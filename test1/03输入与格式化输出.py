# 输入  input 注:python3将输入内容都存为str
name1 = input('请输入:')
print(name1)
# 格式化字符串输出
# # (1) %s 可以传任意值进去，都可以当作str
name = 'Xiao Wang'
age = '10'
print('my name is %s,age is %s' % (name, age))
print('my name is %(2)s,age is %(1)s' % {"1": age, "2": name})
# # (2) format()
print('my name is {},age is {}'.format(name, age))
print('my name is {1},age is {0}'.format(name, age))
print('my name is {b},age is {b}'.format(a=age, b=name))
# # # 格式化填充
print('{:*^10}'.format('字符串'))
print('{:*>10}'.format('字符串'))
print('{:*<10}'.format('字符串'))
b = '{:.2f}'.format(3.1415926)
print(b,type(b))
# # (3) f
print(f"我的名字是{name}，我今年{age}岁了") 
