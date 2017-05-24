#!/usr/bin/env python
# -*- coding:utf-8 -*-
#在文件的开头定义全局变量
_a = 1
_b = 2
def add():
    global _a
    _a = 3
    return "_a + _b = ",_a + _b

def sub():
    global _b
    _b = 4
    return "_a - _b = ",_a - _b

print(add())
print(sub())
"""
def fun():
    #局部变量
    local = 1
    print(local)

fun()
"""
print("---------------------------")
print(2**38)
print("---------------------------")
print(sum(range(1,101)))
print("---------------------------")
print reduce(lambda a,b:a+b,range(1,101))
print("---------------------------")
n = 0
for i in range(101):
    n = n + i
print n