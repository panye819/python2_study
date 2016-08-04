#coding=utf-8
                                                                                                                                                                                   
#导入模块，urllib2是一个模拟浏览器HTTP方法的模块
import json
import urllib2
import sys
from urllib2 import URLError, HTTPError
                                                                                                                                                                                   
#url and url header
#zabbix的api 地址，用户名，密码，这里修改为自己实际的参数
zabbix_url="http://10.0.0.232/zabbix/api_jsonrpc.php"
zabbix_header = {"Content-Type":"application/json"}
zabbix_user   = "Admin"
zabbix_pass   = "zabbix"
auth_code     = ""
                                                                                                                                                                                   
#auth user and password
#用户认证信息的部分，最终的目的是得到一个SESSIONID
#这里是生成一个json格式的数据，用户名和密码
auth_data = json.dumps(
        {
            "jsonrpc":"2.0",
            "method":"user.login",
            "params":
                    {
                        "user":zabbix_user,
                        "password":zabbix_pass
                    },
            "id":0
        })
                                                                                                                                                                                   
# create request object
request = urllib2.Request(zabbix_url,auth_data)
for key in zabbix_header:
    request.add_header(key,zabbix_header[key])
                                                                                                                                                                                   
#auth and get authid
try:
    result = urllib2.urlopen(request)
#对于出错新的处理
except HTTPError, e:
    print 'The server couldn\'t fulfill the request, Error code: ', e.code
except URLError, e:
    print 'We failed to reach a server.Reason: ', e.reason
else:
    response=json.loads(result.read())
    result.close()
'''
　　如果访问成功或者失败，这里的数据会显示如下
    sucess result:
        {"jsonrpc":"2.0",
         "result":"0d225d8d2a058625f814f3a0749cd218",
         #result后面的值是SESSIONID，每次去访问都会发生变化的
         "id":0}
    error  result:
        {'code': -32602,
         'data': 'Login name or password is incorrect.',
         'message': 'Invalid params.'}
　　'''
    
#判断SESSIONID是否在返回的数据中
if  'result'  in  response:
    auth_code=response['result']
else:
    print  response['error']['data']
                                                                                                                                                                                    
# request json
#用得到的SESSIONID去通过验证，获取主机的信息（用http.get方法）
if len(auth_code) == 0:
    sys.exit(1)
if len(auth_code) != 0:
    get_host_data = json.dumps(
    {
        "jsonrpc":"2.0",
        "method":"host.get",
        "params":{
                "output": "extend",
        },
        "auth":auth_code,
        "id":1,
    })
                                                                                                                                                                                    
    # create request object
    request = urllib2.Request(zabbix_url,get_host_data)
    for key in zabbix_header:
        request.add_header(key,zabbix_header[key])
                                                                                                                                                                                    
    # get host list
    try:
        result = urllib2.urlopen(request)
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server could not fulfill the request.'
            print 'Error code: ', e.code
    else:
        response = json.loads(result.read())
        result.close()
                                                                                                                                                                                          
        #将所有的主机信息显示出来
        print response
        #显示主机的个数
        print "Number Of Hosts: ", len(response['result'])
