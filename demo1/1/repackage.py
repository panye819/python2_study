# -*- coding:utf-8 -*- 
'''
Created on 2016年7月27日
@author: bluebell325
'''
import os
import tarfile
import shutil
#获取用户输入的aqy.tar.gz路径并解压
a=os.name
print a
b=os.getcwd()
print b
aqy_file_location=os.path.abspath(raw_input("请输入安全易安装文件存放路径: "))
#print aqy_file_location
os.chdir(aqy_file_location)
c=os.getcwd()
#print c
d=os.listdir(c)
#print d
#print d[0]
tar=tarfile.open(d[0])
names = tar.getnames()
for name in names:
    tar.extract(name,path=".")
tar.close()
print "安装包已解压完成！"
d1=os.listdir(c)
print d1
shutil.move("aqy.tar.gz", "d:\\aqy.tar.gz")
d2=os.listdir(c)
print d2
