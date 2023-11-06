# 整数 int    int(纯数字字符串)
# 浮点型 float
# 字符串类型 str : 'xxx' "xxx"  """xxx"""
print("-" * 10, 'nan', "-" * 10)
# 列表 []   存放变量为间接引用，索引寻找的变量的内存地址
# 字典 dict   dict={key:value,......}
# 布尔型 bool True False:0,None,'',{}.[]
# 垃圾回收机制：引用计数、标记清除、分代回收
# # 循环引用导致内存泄漏 ，标记清除会检索栈区与堆区，没有栈区变量引用的内存地址标记为死亡

# 可变类型 :值改变，id不变
"""列表 字典"""
# 不可变类型 :值改变，id不变
"""str int float """

# 深度拷贝与浅拷贝
"""
浅拷贝
l3=l1.copy()
l3不可变类型改变l1不可变类型不变
l3可变类型改变其中的值l1不可变类型改变
深拷贝 都不变
例子：
import copy
l1 = [11, 2, 3, [1, 2, 3]]
l3 = copy.deepcopy(l1)
print(l1)
print(l3)
l3[3][2] = 5
print(l1)
print(l3)
l2=l1.copy()
l2[3][2] = 2
print(l1)
print(l2)
"""
