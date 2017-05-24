#!/usr/bin/env python
# -*- coding:utf-8 -*-
def func():
    print ("myModule.func()")

class MyClass:
    def myFunc(self):
        print ("MyModule.MyClass.myFunc()")

func()

if __name__ == '__main__':
    print ("myModule作为主程序运行")
else:
    print ("pack2初始化")
