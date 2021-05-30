
# abs 取绝对值
print(abs(-1))
# all 可迭代对象都真
# any 其中一个真

# bin 十进制转二进制
# oct 转八进制
# hex 转十六进制

# chr aci转字符
# ord 反过来

# dir 查看有哪些属性

# divmod(10,3) ===>(3,1)商，余数
# enumerate
for i,v in enumerate(['a','b','c']):
    print(i,v)   # 索引和值

# eval 执行字符串中的表达式，将字符串中的某个类型转换成对应类型

#frozenset 不可变集合
# hash(不可变类型)
#isinstance() 判断一个对象是不是一个类的实例
#isinstance(obj,Foo) 类型判断

# print(pow(10,2,3)) 10 ** 2 % 3
# round() 四舍五入

l1 = ['a','b','c','d']
l2 = [1,2,3,4,5]
# 顾头不顾尾，步长
# l1[1:4:2]
# l2[1:4:2]

# zip
v1 = 'hello'
v2 = [1,2,3,4,5]
print(list(zip(v1,v2)))
#[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]


__import__()