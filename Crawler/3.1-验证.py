from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm #验证
from urllib.error import URLError
from urllib import parse,request
from urllib.request import build_opener
username = 'username'
password = 'password'
#url = "http://127.0.0.1"
url = "http://httpbin.org/post"
data=bytes(parse.urlencode({'word':"hello"}),encoding="utf8")
header={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
requ=request.Request(url,data=data,headers=header,method="POST")
p = HTTPPasswordMgrWithDefaultRealm()
print(p, type(p))
p.add_password(None, url, username, password)
print(p, type(p))
auth_handler = HTTPBasicAuthHandler(p)
print(auth_handler, type(auth_handler))
opener = build_opener(auth_handler)
print(opener, type(opener))
try:
    response = opener.open(requ,timeout=1)
    print(response, type(response))
    html = response.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)

