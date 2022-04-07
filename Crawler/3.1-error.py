from urllib import request,error

try:
    response=request.urlopen('https://cuiqingcai.com/index.htm',timeout=0.01)
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason,type(e.reason),sep='\n')
else:
    print('request susscssfully')