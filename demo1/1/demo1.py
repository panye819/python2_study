# -*- coding:utf-8 -*- 
'''
Created on 2016��7��20��
@author: bluebell325
'''
""""
from fileinput import filename
print "Welcome to python world!"
print "欢迎光临！！"
a=1
b=2
c=a+b
print c
i=0
while i<10:
    print i
    i+=1
else:
    print "out!"

filename=raw_input("Enter file name: ")
fobj=open(filename,'r')
for eachLine in fobj:
    print eachLine
fobj.close()

i=2
while i <= 101:
    print i
    i+=1
print "2-------------------"
i=1
while i < 100:
    if i%2 == 1:        
        print i
    i+=1

i=0
while i<11:
    print i
    i+=1 
a=range(0,11)
for x in a:
    print x

num1=eval(raw_input("Please input a numner: "))
if num1 >0:
    print "This number is 正数！" 
else:
    print "This number is 负数！"
"""
