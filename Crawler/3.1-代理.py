from urllib.request import ProxyHandler, build_opener
from urllib import request,parse
from urllib.error import URLError
proxy_handler = ProxyHandler({
   'http': 'http://127.0.0.1',
    'https': 'https://127.0.0.1'
})
url = "https://www.baidu.com"
data=bytes(parse.urlencode({'word':"hello"}),encoding="utf8")
header={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
requ=request.Request(url,data=data,headers=header,method="POST")
opener = build_opener(proxy_handler)
try:
    response = opener.open(requ,timeout=1)
    print(response, type(response))
    html = response.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
