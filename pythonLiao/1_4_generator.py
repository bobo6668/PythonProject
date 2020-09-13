# -*- coding: utf-8 -*-

def triangles():  # 参考代码
    x = [1]  # 第一次
    while True:
        yield x  # 【重点理解】在执行过程中，遇到yield就中断并返回，下次又从此处开始继续执行。
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
