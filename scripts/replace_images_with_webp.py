#!/usr/bin/env python3
"""
🔄 Markdown 图片引用 WebP 替换工具

功能：
- 自动检测 Markdown 文件中的图片引用
- 检查对应的 WebP 文件是否存在
- 将图片引用替换为 WebP 格式
- 支持单个文件或批量处理
- 提供预览和确认模式

使用方法：
python3 scripts/replace_images_with_webp.py [文件或目录] [选项]

选项：
-p, --preview    只预览更改，不实际执行
-r, --recursive  递归处理目录下的所有 Markdown 文件
-f, --force      强制替换，不提示确认
-v, --verbose    显示详细输出
-h, --help       显示帮助信息

示例：
python3 scripts/replace_images_with_webp.py content/post/article.md
python3 scripts/replace_images_with_webp.py content/post -r -p
python3 scripts/replace_images_with_webp.py content -r -f
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

# 颜色输出类
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

class ImageReplacer:
    def __init__(self, preview: bool = False, force: bool = False, verbose: bool = False):
        self.preview = preview
        self.force = force
        self.verbose = verbose
        self.total_files = 0
        self.processed_files = 0
        self.total_replacements = 0
        
        # 正则表达式模式
        # 匹配 Markdown 图片语法: ![alt](image.ext)
        self.markdown_image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+\.(jpg|jpeg|png))\)', re.IGNORECASE)
        # 匹配 Front Matter 中的 image 字段: image: filename.ext
        self.frontmatter_image_pattern = re.compile(r'^(\s*image:\s*)([^\s]+\.(jpg|jpeg|png))(\s*)$', re.IGNORECASE)
        
    def print_colored(self, message: str, color: str = Colors.NC):
        """打印带颜色的消息"""
        print(f"{color}{message}{Colors.NC}")
    
    def webp_exists(self, original_file: str, file_dir: Path) -> bool:
        """检查对应的 WebP 文件是否存在"""
        webp_file = Path(original_file).with_suffix('.webp')
        
        # 检查相对于 Markdown 文件的路径
        webp_path = file_dir / webp_file
        if webp_path.exists():
            return True
        
        # 检查绝对路径（相对于项目根目录）
        project_root = Path(__file__).parent.parent
        absolute_webp_path = project_root / file_dir / webp_file
        if absolute_webp_path.exists():
            return True
        
        return False
    
    def replace_markdown_images(self, line: str, file_dir: Path) -> Tuple[str, int]:
        """替换行中的 Markdown 图片引用"""
        replacements = 0
        modified_line = line
        
        # 查找所有匹配的图片引用
        matches = list(self.markdown_image_pattern.finditer(line))
        
        # 从后往前替换，避免位置偏移问题
        for match in reversed(matches):
            alt_text = match.group(1)
            image_file = match.group(2)
            
            if self.webp_exists(image_file, file_dir):
                webp_file = str(Path(image_file).with_suffix('.webp'))
                # 替换整个匹配的部分
                old_ref = match.group(0)
                new_ref = f"![{alt_text}]({webp_file})"
                modified_line = modified_line[:match.start()] + new_ref + modified_line[match.end():]
                replacements += 1
                
                if self.verbose:
                    self.print_colored(f"  ✓ {image_file} → {webp_file}", Colors.GREEN)
            else:
                if self.verbose:
                    webp_file = str(Path(image_file).with_suffix('.webp'))
                    self.print_colored(f"  ⚠ WebP 不存在: {webp_file}", Colors.YELLOW)
        
        return modified_line, replacements
    
    def replace_frontmatter_images(self, line: str, file_dir: Path) -> Tuple[str, int]:
        """替换 Front Matter 中的图片引用"""
        match = self.frontmatter_image_pattern.match(line)
        if not match:
            return line, 0
        
        prefix = match.group(1)
        image_file = match.group(2)
        suffix = match.group(4)
        
        if self.webp_exists(image_file, file_dir):
            webp_file = str(Path(image_file).with_suffix('.webp'))
            modified_line = f"{prefix}{webp_file}{suffix}"
            
            if self.verbose:
                self.print_colored(f"  ✓ Front Matter: {image_file} → {webp_file}", Colors.GREEN)
            
            return modified_line, 1
        else:
            if self.verbose:
                webp_file = str(Path(image_file).with_suffix('.webp'))
                self.print_colored(f"  ⚠ WebP 不存在: {webp_file}", Colors.YELLOW)
            
            return line, 0
    
    def process_markdown_file(self, md_file: Path) -> None:
        """处理单个 Markdown 文件"""
        file_dir = md_file.parent
        replacements = 0
        
        if self.verbose:
            self.print_colored(f"📄 处理文件: {md_file}", Colors.BLUE)
        
        try:
            # 读取文件内容
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            modified_lines = []
            
            for line in lines:
                original_line = line
                modified_line = line
                line_replacements = 0
                
                # 检查 Markdown 图片语法
                modified_line, md_replacements = self.replace_markdown_images(modified_line, file_dir)
                line_replacements += md_replacements
                
                # 检查 Front Matter 图片引用
                modified_line, fm_replacements = self.replace_frontmatter_images(modified_line, file_dir)
                line_replacements += fm_replacements
                
                modified_lines.append(modified_line)
                replacements += line_replacements
            
            # 如果有替换
            if replacements > 0:
                self.total_replacements += replacements
                
                if self.preview:
                    self.print_colored(f"📋 预览: {md_file} - 发现 {replacements} 个可替换的图片引用", Colors.CYAN)
                else:
                    # 询问是否应用更改（除非是强制模式）
                    apply_changes = True
                    if not self.force:
                        response = input(f"{Colors.YELLOW}❓ 是否应用 {replacements} 个更改到 {md_file}? (y/N){Colors.NC} ")
                        apply_changes = response.lower() in ['y', 'yes']
                    
                    if apply_changes:
                        # 写入修改后的内容
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.writelines(modified_lines)
                        
                        self.print_colored(f"✅ 已更新: {md_file} - 替换了 {replacements} 个图片引用", Colors.GREEN)
                        self.processed_files += 1
                    else:
                        self.print_colored(f"⏭️  跳过: {md_file}", Colors.BLUE)
            else:
                if self.verbose:
                    self.print_colored(f"ℹ️  无需更改: {md_file}", Colors.BLUE)
        
        except Exception as e:
            self.print_colored(f"❌ 处理文件时出错 {md_file}: {e}", Colors.RED)
        
        self.total_files += 1
    
    def find_markdown_files(self, target: Path, recursive: bool = False) -> List[Path]:
        """查找 Markdown 文件"""
        markdown_files = []
        
        if target.is_file():
            if target.suffix.lower() == '.md':
                markdown_files.append(target)
            else:
                self.print_colored(f"⚠️  跳过非 Markdown 文件: {target}", Colors.YELLOW)
        elif target.is_dir():
            if recursive:
                # 递归查找所有 .md 文件
                markdown_files.extend(target.rglob('*.md'))
            else:
                # 只查找当前目录下的 .md 文件
                markdown_files.extend(target.glob('*.md'))
        else:
            self.print_colored(f"❌ 目标不存在: {target}", Colors.RED)
            sys.exit(1)
        
        return sorted(markdown_files)
    
    def process_target(self, target: Path, recursive: bool = False) -> None:
        """处理目标文件或目录"""
        markdown_files = self.find_markdown_files(target, recursive)
        
        if not markdown_files:
            self.print_colored("📝 未找到 Markdown 文件", Colors.YELLOW)
            return
        
        self.print_colored(f"📊 找到 {len(markdown_files)} 个 Markdown 文件", Colors.BLUE)
        
        for md_file in markdown_files:
            self.process_markdown_file(md_file)
    
    def print_statistics(self) -> None:
        """打印统计信息"""
        print()
        self.print_colored("📊 处理统计:", Colors.PURPLE)
        print(f"   • 检查的文件数: {self.total_files}")
        print(f"   • 处理的文件数: {self.processed_files}")
        print(f"   • 总替换次数: {self.total_replacements}")
        
        if self.preview and self.total_replacements > 0:
            print()
            self.print_colored("💡 要实际应用更改，请重新运行脚本并移除 -p 选项", Colors.BLUE)

def main():
    parser = argparse.ArgumentParser(
        description='🔄 Markdown 图片引用 WebP 替换工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s content/post/article.md
  %(prog)s content/post -r -p
  %(prog)s content -r -f
        """
    )
    
    parser.add_argument('target', nargs='?', default='.', 
                       help='目标文件或目录 (默认: 当前目录)')
    parser.add_argument('-p', '--preview', action='store_true',
                       help='只预览更改，不实际执行')
    parser.add_argument('-r', '--recursive', action='store_true',
                       help='递归处理目录下的所有 Markdown 文件')
    parser.add_argument('-f', '--force', action='store_true',
                       help='强制替换，不提示确认')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='显示详细输出')
    
    args = parser.parse_args()
    
    # 创建替换器实例
    replacer = ImageReplacer(
        preview=args.preview,
        force=args.force,
        verbose=args.verbose
    )
    
    # 显示欢迎信息
    replacer.print_colored("🔄 Markdown 图片引用 WebP 替换工具", Colors.CYAN)
    project_dir = Path(__file__).parent.parent
    replacer.print_colored(f"📁 工作目录: {project_dir}", Colors.BLUE)
    
    if args.preview:
        replacer.print_colored("👀 预览模式 - 不会实际修改文件", Colors.YELLOW)
    
    print()
    
    # 处理目标
    target_path = Path(args.target)
    replacer.process_target(target_path, args.recursive)
    
    # 显示统计信息
    replacer.print_statistics()
    
    replacer.print_colored("✅ 完成!", Colors.GREEN)

if __name__ == '__main__':
    main()
