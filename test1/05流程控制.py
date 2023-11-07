# 条件判断

"""
if 条件:
    子代码块(缩进4个空格)
else:
    子代码块
"""
a = 10
if a == 10:
    print('10')
elif a == 11:
    print('12')
else:
    print('11')
print('这是个if结束')

# while 循环
"""num = 0
while num < 5:
    if num + 1 == 2:
        num += 1
        continue
    print(num + 1)
    if num + 1 == 4:
        break
    num += 1"""
# while  else
"""num = 0
while num < 5:
    if num + 1 == 2:
        num += 1
        continue
    print(num + 1)
    if num + 1 == 4:
        break
    num += 1
else:
    print("正常结束循环，没有break")"""
# for循环
"""
遍历格式:

for 变量名 in 可迭代对象:
    子代码块
"""
"""
range()顾头不顾尾
>>>range(10)        # 从 0 开始到 9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
"""