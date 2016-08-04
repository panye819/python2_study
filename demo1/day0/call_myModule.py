# -*- coding:utf-8 -*- 
'''
@author: Lion8308
'''
import myModule
from __builtin__ import file

myModule.func()
myClass=myModule.MyClass()
myClass.myFunc()
def sum1(x=1,y=2):
    return x+y

print apply(sum1,(1,3))

def sum2(x,y):
    return x+y
print reduce(sum1, range(0,10))
print reduce(sum1,range(0,10),10)
print reduce(sum1, range(0,0),10)

f=file("hello.txt","w+")
li=["hello world\n","hello china\n"]
f.writelines(li)
f.close()