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