from urllib import request,parse
from urllib.error import URLError
from http import cookiejar
filename='cookie.txt'
header={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
url="https://www.baidu.com/"
requ=request.Request(url,headers=header)
#cookie = cookiejar.CookieJar()
cookie=cookiejar.LWPCookieJar(filename)
#cookie=cookiejar.MozillaCookieJar(filename)
print(cookie,type(cookie))
handler = request.HTTPCookieProcessor(cookie)
opener=request.build_opener(handler)
response = opener.open(requ,timeout=1)
cookie.save(ignore_discard=True,ignore_expires=True)#
for item in cookie:
    print(item,type(item))
    print(item.name+'='+item.value)
# 下载cookie
# 使用cookie
'''
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
handler=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(handler)
response=opener.open(url)
print(response.read().decode('utf8'))
'''