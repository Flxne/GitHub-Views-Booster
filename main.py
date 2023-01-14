from urllib.request import Request, urlopen
import time

c = 0
req = Request(
    url='',
    headers={'User-Agent': 'Mozilla/4.0'}
)
while True:
    webpage = urlopen(req)
    #time.sleep(0.1)
    c+=1
    print(c)
    webpage.close()
