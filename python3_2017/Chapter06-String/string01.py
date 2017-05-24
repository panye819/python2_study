#!/usr/bin/env python
# -*- coding:utf-8 -*-

str1 = "version"

num = 1.0
format = "%s" % str1

print (format)

format_2 = "%s %d" % (str1,num)

print (format_2)

print ("-------------")
print ("浮点型数字：%f " % 1.25)
print ("浮点型数字：%.1f " % 1.25)
print ("浮点型数字：%.2f " % 1.25)
print ("-------------")
str2 = "Bob said: 1, 2, 3, 4"
print ("使用空格截取子串: ", str2.split())
print ("使用空格截取子串: ", str2.split())
print ("使用逗号截取子串: ", str2.split(","))
print ("使用两个逗号截取子串: ", str2.split(",", 2))
print ("-------------")
str3 = 1
str4 = "1"
if str3 == str4:
    print ("Same!")
else:
    print ("Not Same!")
print ("-------------")
if str(str3) == str4:
    print ("Same")
else:
    print ("Not Same!")

print ("使用空格截取子串")