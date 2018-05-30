import codecs
import re
import requests
import time
from random import randint

books = {}

with open('paloulede', 'rb') as f:
    for line in f:
        c = line.decode().strip().split(',')
        books[c[1].strip()] = c[0].strip()

w = open('urllist2.txt', 'wb')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
for book in books:
    link = books[book]
    prefix = link[18:] + '/'
    source = requests.get(link, headers=headers).text.splitlines()
    count = 0
    for line in source:
        if prefix in line:
            a = re.findall(r'href=\"([^\"]*?)\" >([^<]*?)</a>', line)
            if len(a) != 0:
                print(a)
                count += 1
                w.write((a[0][0] + ',' + a[0][1] + '\n').encode('utf-8'))
    #print('Found ' + count + ' unis in ' + book)
    time.sleep(randint(2,15))
w.close()
