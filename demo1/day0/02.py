# -*- coding:utf-8 -*- 
'''
@author: Lion8308
'''
string1='This is a string'
string2="This is another string"
string3='''This is still another string'''
string4="""And one more string"""
#print type(string1),type(string2),type(string3),type(string4)
""""a=input("a:")
b=input("b:")
if (a>b):
    print a,">",b
else:
    print a,"<",b
a=0
while a<10:
    if a%2==0:
        print a
    a+=1
b=0"""
t1=()
print type(t1)
t2=("apple","banana","grape","orange")
print type(t2),id(t2)
t3=t2
print type(t3),id(t3)
t4=t3[:]
print type(t4),id(t4)
print t4[0]
print t4[-1]
print t4.count("apple")
list1=[1,2,3,4,5,4,3,2,1]
list1.append(0)
#list1.pop(-2)
list1.sort()
list1.reverse()
print list1,".....",list1.count(1)
list2=["apple","banana","grape","orange"]
list2.append("watermelon")
print list2
list2.pop()
print list2
list3=["apple","banana","grape","orange"]
list3.append("watermelon")
print list3
list3.pop(0)
print list3
dict1={"a":"apple","b":"banana","c":"orange"}
dict1["c"]="watermelon"
print dict1,dict1["c"]
for k in dict1:
    print "dict[% s] =" % k,dict1[k]
print dict1.items()
print dict1.keys(),dict1.values(),dict1.get("c"),dict1.get("d","default")
dict2={"g":"blueberry","d":"pear","e":"strawberry"}
dict1.update(dict2)
print dict1
dict3={}
dict3.setdefault("a")
print dict3
dict3["a"]="apple"
dict3.setdefault("a","default")
dict3.setdefault("b")
print sorted(dict2.items(),key=lambda d:d[0])
print dict3   