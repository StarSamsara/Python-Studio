from urllib import request
from urllib import error
from urllib import parse
from urllib import robotparser
import socket

try:
    header={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    data=bytes(parse.urlencode({'word':"hello"}),encoding="utf8")
    url="http://httpbin.org/post"
    # urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,context=None)
    requ=request.Request(url,data=data,headers=header,method='POST')
    response = request.urlopen(requ,timeout=1)
    content = response.read().decode("utf-8")
    print(response,type(response))
    print(response.read(),type(response.read()))
    print(content,type(content))
except error.URLError as e:
    print(type(e))
    if isinstance(e.reason,socket.timeout):
        print(e.reason)

'''
<class 'http.client.HTTPResponse'>
包含read(),readinto(),getheader(name),getheaders(),fileno()等方法
以及msg,version,status,reason,debuglevel,closed等属性
'''
