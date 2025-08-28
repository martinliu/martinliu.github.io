---
author:
- '[[Matías Salinas]]'
created: 2025-08-27
description: 如果你是一个多年从事云计算基础设施 (Cloud Infrastructure)、SRE 和应用数据科学 (Applied Data Science)
  工作的人，你一定很欣赏 Python 提供的清晰和简洁。无论你是在原型设计一个机器学习…
original_lang: en
published: 2025-05-06
source: https://msalinas92.medium.com/i-made-my-python-code-10x-faster-using-these-little-known-tricks-that-most-developers-ignore-72d36d097b60
tags:
- clippings
target_lang: zh-CN
title: 用这些鲜为人知（且大多数开发者都忽略）的技巧，让你的 Python 代码提速 10 倍
translated: true
translation_date: '2025-08-28'
---




如果你是一名在云计算基础架构 (cloud infrastructure)、SRE (Site Reliability Engineering) 和应用数据科学领域工作的从业者，你一定很欣赏 Python 提供的清晰性和简洁性。无论你是在原型化机器学习模型、编排后端工作流，还是在生产级系统 (production-grade system) 中构建自动化管道，Python 始终是你工具库中的首选。但说实话—— **Python 有时会很慢**。慢得令人痛苦。

![Python](0_VXY46SwRfsnWJKIC.webp)

然而，你需要了解并牢记的是，**Python 的大多数性能问题都是开发者自己造成的**。问题不在于语言本身，而在于你使用它的方式。事实上，Python 的瓶颈往往是由被忽视的细节引起的：低效的数据结构 (data structures)、不必要的内存分配 (allocations)、重复的计算 (redundant computations)，或者仅仅是你从其他语言带来的、不完全适用的习惯。

你可能见过太多的工程师（尤其是在高性能计算 (high-performance computing) 领域之外）低估了一些小决定的成本。比如循环方式不当、内置函数使用效率低下、忽视性能分析 (profiling)，或者过度依赖 Pandas (Pandas) 来执行本可以使用 NumPy (NumPy) 或 Polars (Polars) 提速 50 倍的操作。更别提那些仍然在 Pandas 中使用 ``apply`` 而不是向量化 (vectorization) 的人了。

在这篇文章中，作者不会谈论你随处可见的那些显而易见的建议，比如"使用 NumPy"或"避免 for 循环"。这些你都听过了。这是一次**深入探讨那些被低估、被忽视、有时甚至有些奇特的技巧，它们能够显著加速你的 Python 代码**——这些技巧你真希望能早点知道。本文将通过实际案例、你可能没用过（但应该用）的库，以及那些悄悄侵蚀你性能的习惯，为你一一讲解。

所以，如果你正在处理大型数据管道 (data pipelines)、后端 API (Application Programming Interface)、科学计算 (scientific computing)，甚至是自动化基础架构 (infrastructure) 的工作——并且你觉得 Python 正在拖累你——那么这篇文章就是为你准备的。

## 🚀 1. 停止使用 range(len(...)) — 改用 enumerate

这看起来可能微不足道，但在某些紧密的循环中，它却出乎意料地常见且代价高昂：

```python
# Slow
for i in range(len(my_list)):
    value = my_list[i]

# Faster and more Pythonic
for i, value in enumerate(my_list):
    ...
```

使用 ``enumerate``（枚举）可以避免重复的索引和方法调用。它更简洁，并有助于解释器在底层进行更好的优化。

## ⚡ 2. 避免将 list 用于大型集合 — 改用 array、deque 或 numpy 数组

Python 列表 (lists) 通用且灵活，但对于大型数值运算来说，它们的**内存效率不高**且速度不快。

```python
from array import array
my_array = array('i', [1, 2, 3, 4])  # Much faster than list for ints
```

或者更好的是，对数值数据使用 `numpy` 或 `polars.Series`。NumPy 使用由 C 语言支持的固定类型数组，而 Polars（见下文）是用 Rust 编写的，并针对速度进行了优化。

## 🧠 3. 使用 functools.lru\_cache 加速纯函数

如果你有计算开销大的纯函数（即，相同输入 → 相同输出），记忆化 (memoization) 可以带来显著的性能提升：

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x, y):
    ...
```

这在许多机器学习 (Machine Learning) 管线中被严重低估。

## 🏁 4. 使用 Numba 将 Python 编译成机器码 — 无需更改代码

这是一个改变游戏规则的工具。

```python
from numba import jit

@jit(nopython=True)
def compute(x):
    ...
```

被 `@jit` 包装的函数可以运行得**快 100 倍**。Numba 使用 LLVM 编译你的代码，只需极少的语法改动。它最适用于循环和数值计算代码。

## ⚙️ 5. 将 Pandas 切换到 Polars 处理 DataFrame

Pandas 很棒。但对于大型数据集来说，它速度慢且是单线程的。此时，让开发者引入 `[Polars](https://pola.rs/)`，一个用 Rust 编写并支持原生多线程的极速 DataFrame 库。

```python
import polars as pl
df = pl.read_csv("data.csv")
df = df.filter(pl.col("sales") > 1000)
```

在实际的 ETL (Extract, Transform, Load) 管线中，Polars 的性能可以比 Pandas **高 10 倍甚至更多**。

## 🔍 6. 使用内置性能分析工具 — 不要盲目优化

在优化任何东西之前，请先进行**性能分析 (Profiling)**。你无法改进无法衡量的事物。

```bash
python -m cProfile my_script.py
```

或者更好的是，使用 `line_profiler`：

```bash
pip install line_profiler
```

```python
@profile
def my_func():
    ...
```

然后使用以下命令运行：

```bash
kernprof -l my_script.py
python -m line_profiler my_script.py.lprof
```

这显示了逐行的瓶颈，是性能调试 (Performance Debugging) 的利器。

## ⛏️ 7. 在紧密循环中最小化属性查找

这一个细微但非常真实：

```python
# Bad
for _ in range(1000000):
    value = my_object.some_attribute

# Better
attr = my_object.some_attribute
for _ in range(1000000):
    value = attr
```

每一次属性访问 (attribute access) 都是一次字典查找 (dictionary lookup)。在大型循环中，这会累积起来。

## 🧬 8. 预分配列表而不是在循环中追加

追加操作方便，但在大规模操作时会很慢：

```python
# Slow
result = []
for i in range(1000000):
    result.append(i)

# Faster
result = [None] * 1000000
for i in range(1000000):
    result[i] = i
```

这在数据预处理中尤为重要。

## 📦 9. 尝试 Pydantic V2 (或 msgspec) 进行快速数据验证

如果你正在构建 API (Application Programming Interface) 或摄取数据，你可能正在使用 Pydantic。但 v2 **用 Rust 重写**，速度快得多：

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
```

或者，为了极致性能：

```python
import msgspec

class User(msgspec.Struct):
    id: int
    name: str
```

`msgspec` 比 Pydantic 和 dataclasses 都快。

## 🧪 10. 尽可能使用生成器而不是列表

如果你不需要一次性获取所有结果，请使用生成器 (Generators)：

```python
def slow():
    return [x**2 for x in range(10**6)]

def fast():
    return (x**2 for x in range(10**6))
```

内存使用量将从千兆字节降到几乎为零。

## ⚙️ 额外提示：使用 mypyc 编译你的脚本 (实验性但有前景)

如果你的模块中使用了类型提示 (type hints)：

```bash
pip install mypy mypyc

# Compiles your script to C extension
mypyc my_module.py
```

这对于数值计算代码尤其强大，而且如果你已经在使用类型标注 (typing)，只需要进行极小的改动。

## 最终思考

大多数开发者认为 Python 运行缓慢。然而，如果使用得当，Python 的速度会**出人意料地快**。真正的瓶颈不在于语言本身，而在于我们的使用习惯。通过结合智能利用原生特性、未被充分利用的库以及性能优先的思维模式，我们可以在高吞吐量的生产工作负载中，也能实现全新的速度水平。

在自己的案例中，优化了生产环境中几个关键的推理评分和数据转换流水线，将运行时间从**数分钟缩短到数秒**。最棒的是什么？不要更换语言，也不要用 C++ 重写一切。你只需要开始将 Python 视为它本应有的强大语言——只要使用得当。

如果你认真想要从 Python 中榨取性能，请从这些建议开始。然后进行性能分析 (profile)、测试，并持续学习。总会有更快的方法。
