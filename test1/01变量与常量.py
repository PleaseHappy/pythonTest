# 变量值
name = '李雷'
# id
print(id(name))  # 查看id
# type
print(type(name))  # 查看type
# is 与 ==
a = '李雷'
b = '李雷'
print(id(a), id(b))  # pycharm会进行优化导致结果一样，事实上不一样
print(a == b)
print(a is b)
# 但对于整数（-5至256的最小整数池）来说来说id相同
# 规范上可以用全大写表示常量