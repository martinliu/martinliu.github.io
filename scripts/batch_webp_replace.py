#!/usr/bin/env python3
"""
🚀 批量 WebP 替换处理脚本

这是一个便捷的脚本，用于批量处理博客中的图片引用替换。
它会自动处理常见的目录，并提供安全的预览和确认流程。

使用方法：
python3 scripts/batch_webp_replace.py [选项]

选项：
--preview-only   只预览，不执行任何实际替换
--force-all      强制替换所有，不询问确认
--verbose        显示详细输出
"""

import argparse
import subprocess
import sys
from pathlib import Path

class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'

class BatchWebPReplacer:
    def __init__(self, preview_only=False, force_all=False, verbose=False):
        self.preview_only = preview_only
        self.force_all = force_all
        self.verbose = verbose
        self.script_path = Path(__file__).parent / "replace_images_with_webp.py"
        
        # 要处理的目录列表（按优先级排序）
        self.target_directories = [
            "content/post",
            "content/page",
            "content"
        ]
    
    def print_colored(self, message: str, color: str = Colors.NC):
        """打印带颜色的消息"""
        print(f"{color}{message}{Colors.NC}")
    
    def run_replacement(self, directory: str, preview: bool = False) -> tuple:
        """运行替换脚本并返回结果"""
        cmd = ["python3", str(self.script_path), directory, "-r"]
        
        if preview:
            cmd.append("-p")
        else:
            cmd.append("-f")  # 强制模式，不逐个询问
            
        if self.verbose:
            cmd.append("-v")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # 解析统计信息
            lines = result.stdout.split('\n')
            total_files = 0
            processed_files = 0
            total_replacements = 0
            
            for line in lines:
                if "检查的文件数:" in line:
                    total_files = int(line.split(':')[1].strip())
                elif "处理的文件数:" in line:
                    processed_files = int(line.split(':')[1].strip())
                elif "总替换次数:" in line:
                    total_replacements = int(line.split(':')[1].strip())
            
            return (total_files, processed_files, total_replacements, result.stdout)
        
        except subprocess.CalledProcessError as e:
            self.print_colored(f"❌ 处理 {directory} 时出错: {e}", Colors.RED)
            if e.stderr:
                print(e.stderr)
            return (0, 0, 0, "")
    
    def process_directory(self, directory: str):
        """处理单个目录"""
        dir_path = Path(directory)
        if not dir_path.exists():
            self.print_colored(f"⚠️  目录不存在，跳过: {directory}", Colors.YELLOW)
            return
        
        self.print_colored(f"\n📁 处理目录: {directory}", Colors.BLUE)
        
        # 首先运行预览
        self.print_colored("🔍 预览扫描中...", Colors.CYAN)
        total_files, _, total_replacements, _ = self.run_replacement(directory, preview=True)
        
        if total_replacements == 0:
            self.print_colored(f"✅ {directory} - 无需替换 (检查了 {total_files} 个文件)", Colors.GREEN)
            return
        
        self.print_colored(f"📊 发现 {total_replacements} 个可替换的图片引用 (共 {total_files} 个文件)", Colors.YELLOW)
        
        if self.preview_only:
            self.print_colored("👀 预览模式 - 跳过实际处理", Colors.BLUE)
            return
        
        # 询问是否继续
        if not self.force_all:
            response = input(f"{Colors.YELLOW}❓ 是否处理 {directory} 目录? (y/N){Colors.NC} ")
            if response.lower() not in ['y', 'yes']:
                self.print_colored("⏭️  跳过此目录", Colors.BLUE)
                return
        
        # 执行实际替换
        self.print_colored("🔄 执行替换中...", Colors.CYAN)
        _, processed_files, actual_replacements, output = self.run_replacement(directory, preview=False)
        
        if actual_replacements > 0:
            self.print_colored(f"✅ 完成! 处理了 {processed_files} 个文件，替换了 {actual_replacements} 个图片引用", Colors.GREEN)
        else:
            self.print_colored("ℹ️  没有文件被修改", Colors.BLUE)
    
    def run(self):
        """运行批量处理"""
        self.print_colored("🚀 批量 WebP 替换处理工具", Colors.CYAN)
        self.print_colored(f"📁 工作目录: {Path.cwd()}", Colors.BLUE)
        
        if self.preview_only:
            self.print_colored("👀 预览模式 - 不会修改任何文件", Colors.YELLOW)
        elif self.force_all:
            self.print_colored("⚡ 强制模式 - 将自动处理所有目录", Colors.YELLOW)
        
        # 检查脚本是否存在
        if not self.script_path.exists():
            self.print_colored(f"❌ 找不到替换脚本: {self.script_path}", Colors.RED)
            sys.exit(1)
        
        total_overall_replacements = 0
        
        # 处理每个目录
        for directory in self.target_directories:
            try:
                self.process_directory(directory)
            except KeyboardInterrupt:
                self.print_colored("\n\n⚠️  用户中断操作", Colors.YELLOW)
                break
            except Exception as e:
                self.print_colored(f"❌ 处理目录 {directory} 时出现错误: {e}", Colors.RED)
                continue
        
        self.print_colored("\n🎉 批量处理完成!", Colors.GREEN)
        
        if self.preview_only:
            self.print_colored("\n💡 要实际执行替换，请使用：", Colors.BLUE)
            self.print_colored("   python3 scripts/batch_webp_replace.py", Colors.BLUE)
            self.print_colored("   或", Colors.BLUE)
            self.print_colored("   python3 scripts/batch_webp_replace.py --force-all", Colors.BLUE)

def main():
    parser = argparse.ArgumentParser(
        description='🚀 批量 WebP 替换处理脚本',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--preview-only', action='store_true',
                       help='只预览，不执行任何实际替换')
    parser.add_argument('--force-all', action='store_true',
                       help='强制替换所有，不询问确认')
    parser.add_argument('--verbose', action='store_true',
                       help='显示详细输出')
    
    args = parser.parse_args()
    
    # 防止同时使用 preview-only 和 force-all
    if args.preview_only and args.force_all:
        print(f"{Colors.RED}❌ --preview-only 和 --force-all 不能同时使用{Colors.NC}")
        sys.exit(1)
    
    replacer = BatchWebPReplacer(
        preview_only=args.preview_only,
        force_all=args.force_all,
        verbose=args.verbose
    )
    
    replacer.run()

if __name__ == '__main__':
    main()
