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
