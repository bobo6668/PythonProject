# Python高级特性

> [Python高级特性 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269809315232)

**基本思想**：在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

[toc]

## 1. 切片

`L[0:3]` 表示，从索引`0`开始取，直到索引`3`为止，但不包括索引`3`。即索引`0`，`1`，`2`，正好是3个元素。

Python支持 `L[-1]` 取倒数第一个元素，而且支持倒数切片（逆序）。

甚至什么都不写，只写`[:]`就可以原样复制一个list

**练习题**：`1_1_Slice.py`

利用切片操作，实现一个`trim()`函数，去除字符串首尾的空格，注意不要调用`str`的`strip()`方法：

```python
# -*- coding: utf-8 -*-
def trim(s):
    # if s != '':
    #     while s[0] == ' ': # 要求s至少有一个元素，如果遇到''，会报错IndexError: string index out of range
    #         s = s[1:]
    #     while s[-1] == ' ':
    #         s = s[:-1]
    # return s
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
```

## 2. 迭代

在Python中，迭代是通过`for ... in`来完成的。而很多语言比如C语言，迭代list是通过下标完成的

也就是说，**Python的`for`循环抽象程度要高于C的`for`循环**。因为Python的`for`循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

那么，**如何判断一个对象是可迭代对象呢？**方法是通过`collections`模块的`Iterable`类型判断：

```python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

**如果要对`list`实现类似`Java`那样的下标循环怎么办？**Python内置的`enumerate`函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```

**练习题**：`2_2_For.py`

请使用迭代查找一个`list`中最小和最大值，并返回一个`tuple`：

```python
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    my_max = None
    my_min = None
    if L is None: # 特殊处理 L是None的情况
        return None, None
    else:
        for i in L:
            if my_max is None and my_min is None: # 初始化
                my_max = i
                my_min = i
            else:
                if i > my_max:
                    my_max = i
                if i < my_min:
                    my_min = i
        return my_min, my_max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
```

