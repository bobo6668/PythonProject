# （笔记）廖老师 1 Python高级特性

> [Python高级特性 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269809315232)

**基本思想**：在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

[TOC]

## 1.1 切片

> [Python高级特性 - 切片 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856)

`L[0:3]` 表示，从索引`0`开始取，直到索引`3`为止，但不包括索引`3`。即索引`0`，`1`，`2`，正好是3个元素。

Python支持 `L[-1]` 取倒数第一个元素，而且支持倒数切片（逆序）。

甚至什么都不写，只写`[:]`就可以原样复制一个list

### 练习：`1_1_Slice.py`

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



## 1.2 迭代

> [Python高级特性 - 迭代 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017316949097888)

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

### 练习：`1_2_For.py`

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



## 1.3 列表生成式

> [Python高级特性 - 列表生成式 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776)

列表生成式即List Comprehensions

如果要**生成`[1x1, 2x2, 3x3, ..., 10x10]`**怎么做？

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**for循环后面还可以加上if判断**，这样我们就可以筛选出仅偶数的平方：

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

还可以**使用两层循环**，可以生成全排列：

```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

使用列表生成式的时候，有些童鞋经常搞不清楚**`if...else`的用法**

例如，以下代码正常输出偶数：

```python
>>> [x for x in range(1, 11) if x % 2 == 0]
[2, 4, 6, 8, 10]
```

**情况1：**但是，我们不能在最后的`if`加上`else`：

```python
>>> [x for x in range(1, 11) if x % 2 == 0 else 0]
  File "<stdin>", line 1
    [x for x in range(1, 11) if x % 2 == 0 else 0]
                                              ^
SyntaxError: invalid syntax
```

**这是因为跟在`for`后面的`if`是一个筛选条件，不能带`else`**，否则如何筛选？

**情况2：**另一些童鞋发现把`if`写在`for`前面必须加`else`，否则报错：

```python
>>> [x if x % 2 == 0 for x in range(1, 11)]
  File "<stdin>", line 1
    [x if x % 2 == 0 for x in range(1, 11)]
                       ^
SyntaxError: invalid syntax
```

**这是因为`for`前面的部分是一个表达式，它必须根据`x`计算出一个结果。**

因此，考察表达式：`x if x % 2 == 0`，它无法根据`x`计算出结果，因为缺少`else`，必须加上`else`：

```python
>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
```

上述`for`前面的表达式`x if x % 2 == 0 else -x`才能根据`x`计算出确定的结果。

**小结：**

可见，在一个列表生成式中，`for`前面的`if ... else`是表达式，而`for`后面的`if`是过滤条件，不能带`else`。

### 练习：`1_3_list.py`

如果list中既包含字符串，又包含整数，由于非字符串类型没有`lower()`方法，所以列表生成式会报错：

请修改列表生成式，通过添加`if`语句保证列表生成式能正确地执行：

```python
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() if isinstance(x, str) else x for x in L1]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
```

```python
['hello', 'world', 'apple']
测试通过!
```



## 1.4 生成器

> [Python高级特性 - 生成器 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128)

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，会占用很大的存储空间

试试不创建完整的list，从而节省大量的空间？**在Python中，这种一边循环一边计算的机制，称为生成器：generator。**

**创建一个generator**，有很多种方法。

### 法1：改`[]`为`()`

很简单，只要把一个列表生成式的`[]`改成`()`，就创建了一个generator：

```python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

创建`L`和`g`的区别仅在于最外层的`[]`和`()`，`L`是一个list，而`g`是一个generator。

我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过`next()`函数获得generator的下一个返回值：但是更好的是用`for`循环

```python
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
... 
0
1
4
9
16
25
36
49
64
81
```

所以，我们创建了一个generator后，基本上永远不会调用`next()`，而是通过`for`循环来迭代它，并且不需要关心`StopIteration`的错误。

### 法2：`yield`关键字

定义generator的另一种方法。如果一个函数定义中包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个generator：

**在执行过程中，遇到`yield`就中断，下次又继续执行。**

把函数改成generator后，我们基本上从来不会用`next()`来获取下一个返回值，而是直接使用`for`循环来迭代：

### 练习：`1_4_generator.py`

[杨辉三角](http://baike.baidu.com/view/7804.htm)定义如下：

```ascii
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
```

把每一行看做一个list，试写一个generator，不断输出下一行的list：

```python
# -*- coding: utf-8 -*-

def triangles():  # 参考代码
    x = [1]  # 第一次
    while True:
        yield x  # 【重点理解】在执行过程中，遇到yield就中断并返回，下次又从此处开始继续执行
        y = [0] + x + [0]  # 学到了：① 先根据旧的x构造一个临时的y
        x = [y[i] + y[i + 1] for i in range(len(y) - 1)]  # ② 再根据y构造新的x
    pass


# 开始测试
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
```

**注意区分普通函数和generator函数**：

普通函数调用直接返回结果：

```
>>> r = abs(6)
>>> r
6
```

generator函数的“调用”实际返回一个generator对象：

```
>>> g = fib(6)
>>> g
<generator object fib at 0x1022ef948>
```

## 1.5 迭代器

> [Python高级特性 - 迭代器 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640)

### 可迭代对象：`Iterable`

可以直接作用于`for`循环的对象统称为**可迭代对象：`Iterable`**

包括：

* 集合数据类型
  * 如`list`、`tuple`、`dict`、`set`、`str`等
* generator
  * 包括生成器、带`yield`的generator function

可以使用`isinstance()`**判断**一个对象是否是`Iterable`对象：

```python
>>> from collections.abc import Iterable  # 【记】
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

### 迭代器：`Iterator`

可以被`next()`函数调用并不断返回下一个值的对象称为**迭代器：`Iterator`**

可以使用`isinstance()`**判断**一个对象是否是`Iterator`对象：

```python
>>> from collections.abc import Iterator  # 【记】
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

**生成器都是`Iterator`对象**，可以被`next()`函数调用并不断返回下一个值。

**但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。**

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

**为什么** `list`、`dict`、`str`等数据类型不是`Iterator`？

因为`Iterator`的计算是**惰性**的，只有在需要返回下一个数据时它才会计算。

`Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

### 小结

* 凡是可作用于`for`循环的对象都是`Iterable`类型；
* 凡是可作用于`next()`函数的对象都是`Iterator`类型，它们表示一个惰性计算的序列；
* 集合数据类型如`list`、`dict`、`str`等是`Iterable`但不是`Iterator`，不过可以通过`iter()`函数获得一个`Iterator`对象。
* Python的`for`循环本质上就是通过不断调用`next()`函数实现的。
