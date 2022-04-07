from urllib import parse
url = "https://www.baidu.com/index.html;user?id=5#commet"
# scheme://netloc/path;params?query#fragment
response = parse.urlparse(url)
print(response, type(response))
# print(response[0],response[1],response[2])
# print(response.scheme,response.netloc,response.path)
print(parse.urlunparse(response[0:6]))
print()#
response = parse.urlsplit(url)
print(response, type(response))
print(parse.urlunsplit(response[0:5]))
print()#
print(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
print(parse.urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(parse.urljoin(' http://lwww.baidu.com/about. html',
              'https:///cuiqingcai.com/FAQ.html'))
print(parse.urljoin(' http://www.baidu.com/about.html',
              'https://cuiqingcai.com/FAQ.html?question=2'))
print(parse.urljoin(' http://www.baidu com d=abc', ' https://cuiqingcai.com/index.php'))
print(parse.urljoin(' http://www.baidu.com', '?category=2#comment'))
print(parse.urljoin(' www.baidu.com', '?category=2#comment'))
print(parse.urljoin(' www.baidu.com#coment', '?category=2'))
print()#
params={
    'name':'germey',
    'age':22
}
base_url='https://www.baidu.com?'
url=base_url+parse.urlencode(params)
print(url)
print()#
