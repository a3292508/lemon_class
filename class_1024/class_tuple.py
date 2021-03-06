#!usr/bin/env python
#-*- coding:utf-8 -*-

#元祖，tuple，符号()
#1.可以存在空元祖()
#2.元祖里面可以包含任何类型的数据
#3.元祖里面的元素，用逗号来进行分隔
#4.元祖里的元素也有索引，从0开始
#5.获取元祖里面的单个值：列表[索引值]
#6.元祖的切片，同字符串的操作一致，即元祖名[索引头:索引尾:步长]

#元祖不支持任何修改（增删改）
#操作数据库的时候，可以使用元祖存放条件

tup = (1,'2',True,[3,'john','朱'],'鑫')
print(type(tup))
print(tup)
print(tup[2])
print(tup[-2])
print(tup[2:4])
#元祖不支持任何修改，但可以改动内部的元素,如列表/字典
tup[3][-1] = 'ave'
tup[3].pop()
print(tup)

# 如果元祖里只有一个元素，需要加一个逗号！
a = (1)
b = ('hello')
c = ([1,2,3])
d = ('5',)
print(type(a),type(b),type(c),type(d))