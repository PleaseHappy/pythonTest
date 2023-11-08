# 1.list(可迭代对象) 遍历对象，存每一个值
l = list("hellow world")
print(l)
# 2.追加 append（）
l.append("!")
print(l)
# 3.插入 insert()
l.insert(6, " this")
print(l)
print("".join(l))
# 4.合并
l1 = ['Ni', 'hao']
l3 = "1111111"
l.extend(l3)
print(l)
print(l + l1)  # +不改变原值
print(l)
# 5.删除 del      pop()
del l[6]
print(l)
l.pop()  # 默认删除最后一个  可以返回删除元素 可以按索引删除
# 5.切片  参考字符串
# 6.len()  参考字符串
# 7.count() 统计出现个数
print(l.count("1"))
# 8.index() 统计第一次出现的位置
print(l.index("w"))
# 9.clear()
print(l1)
l1.clear()
print(l1)
# 10.reverse() 反转
l.reverse()
print(l)
l.reverse()
