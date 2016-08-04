# -*- coding:utf-8 -*- 
'''
@author: Lion8308
'''
import os,os.path
"""
def VisitDir(path):
    li=os.listdir(path)
    for p in li:
        pathname=os.path.join(path,p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print pathname

if __name__ == "__main__":
    path=r"E:\git\demo1\day0"
VisitDir(path)"""

def VisitDir(arg,dirname,names):
    for filepath in names:
        print os.path.join(dirname,filepath)

if __name__=="__main__":
    path=r"E:\git\demo1\day0"
    os.path.walk(path, VisitDir, ())