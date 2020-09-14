# （笔记）廖老师 2 Python面向对象
[TOC]

## 2.0 引言

* **面向对象编程**——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把**对象**作为程序的基本单元，一个对象包含了**数据**和**操作数据的函数**。
* **程序设计分类**
  * **面向过程**的程序设计把计算机程序视为<u>一系列的命令集合</u>，即<u>一组函数的顺序执行</u>。
    * 为了简化程序设计，面向过程<u>把函数继续切分为子函数</u>，即把大块函数通过切割成小块函数来降低系统的复杂度。
  * **面向对象**的程序设计把计算机程序视为<u>一组对象的集合</u>，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是<u>一系列消息在各个对象之间传递</u>。

**例子**：假设我们要处理学生的成绩表

**① 面向过程**：

可以用一个`dict` <u>表示一个学生的成绩</u>

```python
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
```

而<u>处理学生成绩</u>可以通过函数实现，比如打印学生的成绩：

```python
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
```

**② 面向对象：**

如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是<u>Student这种数据类型应该被视为一个对象</u>，这个对象<u>拥有name和score这两个属性</u>（Property）。

如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，<u>让对象自己把自己的数据打印出来</u>。

    class Student(object):
        def __init__(self, name, score):
            self.name = name
            self.score = score
    
        def print_score(self):
            print('%s: %s' % (self.name, self.score))

```python
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```

**小结：面向对象的设计思想**是抽象出Class，根据Class创建Instance。 

数据封装、继承和多态是面向对象的三大特点



## 2.1 类和实例

**类**是抽象的模板，比如`Student`类，而**实例**是根据类创建出来的一个个具体的“对象”

### 1）定义类

在Python中，**定义类**是通过`class`关键字：

```python
class Student(object):
    pass
```

其中，类名通常是大写开头的单词；`(object)`，表示该类是从哪个类继承下来的

### 2）创建实例

定义好了`Student`类，就可以根据`Student`类创建出`Student`的实例，**创建实例**是通过`类名+()`实现的：

```python
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>
>>> Student
<class '__main__.Student'>
```

### 3）`__init__`方法

可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的**`__init__`方法**

```python
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数

```python
>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59
```

和普通的函数相比，**在类中定义的函数**只有一点不同，就是第一个参数永远是实例变量`self`，并且，调用时，不用传递该参数。

### 4）数据封装

面向对象编程的一个重要特点就是**数据封装**

可以直接<u>在`Student`类的内部定义访问数据的函数</u>，这样，就把“数据”给封装起来了

“**方法**”就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

如定义函数`print_score`：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
```

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

### P.S.

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```python
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```



## 2.2 访问限制

### 1）私有变量

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个**私有变量（private）**，只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问`实例变量.__name`和`实例变量.__score`了

### 2）外部如何获取变量值？

但是如果外部代码要获取name和score怎么办？可以给Student类增加`get_name`和`get_score`这样的方法：

```python
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
```

### 3）外部如何修改变量值？

如果又**要允许外部代码修改score**怎么办？可以再给Student类增加`set_score`方法：

```python
class Student(object):
    ...

    def set_score(self, score):
        self.__score = score
```

**优点**：可以对参数做检查，避免传入无效的参数：

```python
class Student(object):
    ...

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
```

### P.S.

1）有些时候，你会看到**以一个下划线开头的实例变量名**，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

2）双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量：

```python
>>> bart._Student__name
'Bart Simpson'
```

但是**强烈建议你不要这么干**，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。

3）最后注意下面的这种**错误写法**：

```python
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
```

表面上看，外部代码“成功”地设置了`__name`变量，但实际上这个`__name`变量和class内部的`__name`变量*不是*一个变量！内部的`__name`变量已经被Python解释器自动改成了`_Student__name`，而外部代码给`bart`新增了一个`__name`变量。不信试试：

```python
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
```



## 2.3 继承和多态

### 1）继承

**继承**可以把**父类**的所有功能都直接拿过来，这样就不必重零做起，**子类**只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

比如，我们已经编写了一个名为`Animal`的class，并有一个`run()`方法：

```python
class Animal(object):
    def run(self):
        print('Animal is running...')
```

当我们需要编写`Dog`和`Cat`类时，就可以直接从`Animal`类继承：

```python
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

运行：

```python
dog = Dog()
dog.run()

cat = Cat()
cat.run()
```

运行结果如下：

```python
Animal is running...
Animal is running...
```

可以**改写**子类的`run()`函数

```python
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
```

再次运行，结果如下：

```python
Dog is running...
Cat is running...
```

当子类和父类都存在相同的`run()`方法时，我们说，子类的`run()`**覆盖**了父类的`run()`，在代码运行的时候，总是会调用子类的`run()`。这样，我们就获得了继承的另一个好处：**多态**。

### 2）多态

在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。

如：`dog`的数据类型可以是`Dog`，也可以是`Animal`

要**理解多态的好处**，我们还需要再编写一个函数，这个函数接受一个`Animal`类型的变量：

```python
def run_twice(animal):
    animal.run()
    animal.run()
```

当我们传入`Animal`的实例时，`run_twice()`就打印出：

```python
>>> run_twice(Animal())
Animal is running...
Animal is running...
```

当我们传入`Dog`的实例时，`run_twice()`就打印出：

```python
>>> run_twice(Cat())
Cat is running...
Cat is running...
```

看上去没啥意思，但是仔细想想，现在，如果我们**再**定义一个`Tortoise`类型，也从`Animal`派生：

```
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
```

当我们调用`run_twice()`时，传入`Tortoise`的实例：

```python
>>> run_twice(Tortoise())
Tortoise is running slowly...
Tortoise is running slowly...
```

你会发现，新增一个`Animal`的子类，不必对`run_twice()`做任何修改，实际上，任何依赖`Animal`作为参数的函数或者方法都可以不加修改地正常运行，**原因就在于多态**。

对于一个变量，我们只需要知道它是`Animal`类型，无需确切地知道它的子类型，就可以放心地调用`run()`方法，而具体调用的`run()`方法是作用在`Animal`、`Dog`、`Cat`还是`Tortoise`对象上，由运行时该对象的确切类型决定，这就是**多态真正的威力**：调用方只管调用，不管细节，而当我们新增一种`Animal`的子类时，只要确保`run()`方法编写正确，不用管原来的代码是如何调用的。

这就是**著名的“开闭”原则**：

**对扩展开放**：允许新增`Animal`子类；

**对修改封闭**：不需要修改依赖`Animal`类型的`run_twice()`等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到**根类**object

### 3）动态语言的鸭子类型特点

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

具体：

动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。

对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了：

```python
class Timer(object):
    def run(self):
        print('Start...')
```



## 2.4 获取对象信息

当我们拿到一个对象的引用时，如何知道这个对象**是什么类型**、**有哪些方法**呢？

### 1）* 使用type()

① **基本用法**

**基本类型**都可以用`type()`判断：

```python
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
```

如果一个变量指向**函数或者类**，也可以用`type()`判断：

```python
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>
```

②`type()`函数**返回**的是对应的Class类型。

**判断基本数据类型**可以直接写`int`，`str`等：

```python
>>> type(123)==type(456)
True
>>> type(123)==int
True
```

如果要**判断一个对象是否是函数**怎么办？可以使用**`types`模块**中定义的常量：

```python
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```

### 2）使用isinstance() 【√】

**但是，对于class的继承关系来说，使用`type()`就很不方便。**

我们要判断class的类型，可以使用`isinstance()`函数。

我们回顾上次的例子，如果继承关系是：

```python
object -> Animal -> Dog -> Husky
```

`isinstance()`可以告诉我们，一个对象是否是某种类型。先创建对象：

```python
>>> h = Husky()
```

然后，判断：

```python
>>> isinstance(h, Husky)
True
>>> isinstance(h, Dog)
True
>>> isinstance(h, Animal)
True
```

能用`type()`判断的基本类型也可以用`isinstance()`判断：

```python
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
```

并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

```python
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

因此， **总是优先使用`isinstance()`判断类型**，可以将指定类型及其子类“一网打尽”。

### 3）使用dir()

① 如果要**获得一个对象的所有属性和方法**，可以使用`dir()`函数，它**返回一个包含字符串的list**，比如，获得一个str对象的所有属性和方法：

```python
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
```

② 仅仅把属性和方法列出来是不够的，**配合`getattr()`、`setattr()`以及`hasattr()`**，我们可以直接操作一个对象的状态：

**先定义**类`MyObject`：

```
>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()
```

紧接着，可以**测试该对象的属性**：

```python
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
```

如果试图获取不存在的属性，会抛出AttributeError的错误：

```python
>>> getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'
```

因此，可以传入一个default参数，如果属性不存在，就返回默认值：

```python
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
```

也可以**获得对象的方法**：

```python
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```

**但是，要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息**

### P.S.

```python
print(type(Animal().run))

print(type(Animal().run()))

print(type(Animal.run))
```

输出：

```python
<class 'method'> # 实例的方法

<class 'NoneType'>

<class 'function'> # 类的函数
```



## 2.5 实例属性和类属性

### 1）实例属性

由于Python是动态语言，根据类创建的**实例可以任意绑定属性**。

给实例绑定属性的方法是通过实例变量，或者通过`self`变量：

```Python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```

### 2）类属性

但是，如果`Student`类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归`Student`类所有：

```python
class Student(object):
    name = 'Student'
```

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。

注意到，实例属性优先级比类属性高，会屏蔽掉类的name属性。

在编写程序的时候，**千万不要对实例属性和类属性使用相同的名字**，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

### 练习

为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

```python
# -*- coding: utf-8 -*-
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1  # 每次生成一个实例，就会调用__init__函数，所以可以在这里计数
                            # 但是是用了Student而不是self：
                            	# self.count表示的是实例本身的属性，而不是类属性
                                # 这里计数的是student类的类属性，所以得用 student.count才行


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
```
**小结：**

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。