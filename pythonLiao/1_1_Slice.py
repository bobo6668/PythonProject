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