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