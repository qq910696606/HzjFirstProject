import urllib.request
import math
r=urllib.request.urlopen('http://www.baidu.com')
print(r.status)
print(r.read())


a = 1.56
print(math.floor(a))
print(math.ceil(a))

print(math.sqrt(9))