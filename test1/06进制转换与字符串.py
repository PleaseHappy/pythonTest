# 十进与二进制
print(bin(100))
print(int("0b1100100", 2))
# 十进制与八进制
print(oct(100))
print(int("0o144", 8))
# 十进制与十六进制
print(hex(100))
print(int("0x64", 16))
# float()
print(float(123))
# str()
# 1.索引取值
info = '1hello word1'
print(info[1], info[-3])
# 2.切片（复制一片内容）  取左不取右 [起始:终点:步长]
print(info[::-1])
# 3.strip去除左右两边空格  不改变原值 参数为要去掉的字符，默认为空格
"""lstrip 只去左边 rstrip 只去右边"""
print(info.strip('1'))
print(info)
# 4.split拆分
a = '11 22 33 44'
b = '55==66==77=='
c = a.split()
d = b.split('==', 2)
print(a, '\t', b, '\t', c, '\t', d)
# 5.长度 len()
# 6.lower()小写 upper()大写
# 7.startwith()判断以什么开头返回bool endwith()判断以什么结尾
# 8.join  将字符串（必须字符串）列表拼接
l = ['hello', 'world', '!']
t1 = " qqqq".join(l)
print(t1)
# 9.replace
t2 = t1.replace(" qqqq", " ", 2)
print(t2)
# 10.isdigit 判读字符串是否纯数字字符
print("12".isdigit())
