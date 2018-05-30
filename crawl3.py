import codecs
import re
import requests
requests.adapters.DEFAULT_RETRIES = 3
import time
import random
from random import randint
from requests.exceptions import ProxyError

titles = []

with open('urllist.txt', 'rb') as f:
    for line in f:
        c = line.decode().strip().split(',')
        titles.append(c[0].strip())

foo = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
       "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
       "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
       "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
       "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]
tps = ['185.81.98.125:808',
'178.44.159.142:53281',
'152.157.119.253:3128',
'61.7.190.132:45619',
'78.29.8.83:8080',
'163.44.170.151:8181',
'95.71.250.185:8080',
'147.135.210.114:54566',
'163.44.171.27:8181',
'144.217.248.59:3128',
'163.172.86.64:3128',
'163.44.165.53:8181',
'54.209.135.103:3128',
'163.44.169.65:8181',
'51.15.237.146:3128',
'45.76.133.201:8080',
'206.189.144.133:8080',
'163.44.169.45:8181',
'80.211.189.165:3128',
'163.44.174.118:8181',
'145.249.106.107:8118',
'54.233.85.126:3128',
'202.42.142.66:8080',
       '163.44.172.18:8181',
       '110.5.77.146:8080',
       '163.44.171.181:8181',
       '35.227.54.242:3128',
       '163.44.171.19:8181',
       '159.89.208.224:8118',
       '95.83.21.140:53281',
       '89.22.175.42:8080',
       '153.122.53.124:8118',
       '188.232.209.204:53281',
       '153.122.54.16:8118',
       '188.170.222.130:8080',
       '13.92.196.150:8080',
       '163.44.164.116:8181',
       '177.204.85.203:80',
       '81.14.205.232:8080',
       '167.99.188.36:3128',
       '37.99.36.51:3128',
       '163.44.172.126:8181',
       '94.130.14.146:31288',
       '159.203.116.50:3128',
       '138.201.63.123:31288',
       '163.47.85.222:3128',
       '78.36.39.220:8080',
       '150.242.32.61:53281',
       '202.21.116.186:53281',
       '78.189.65.220:8080',
       '181.112.221.182:53281',
       '153.122.53.233:8118',
       '118.97.234.243:3130',
       '195.208.172.70:8080',
       '195.190.124.202:8080',
       '191.252.100.87:3128',
       '23.97.215.153:3128',
       '66.63.9.26:3128',
       '191.252.195.27:80',
       '41.169.6.195:53281',
       '122.183.139.101:8080',
       '202.93.128.98:3128',
       '95.143.139.149:52136',
       '163.44.167.101:8181',
       '103.241.205.66:8080',
       '157.7.141.56:3128',
       '109.167.215.233:3128',
       '153.122.52.107:8118',
       '153.122.52.77:8118',
       '122.183.139.104:8080',
       '201.46.29.116:8080',
       '212.77.86.103:80',
       '192.116.142.153:8080',
       '117.6.161.118:53281',
       '5.45.64.97:3128',
       '207.32.30.20:8080',
       '178.71.226.11:8080',
       '82.200.44.219:8080',
       '204.48.19.88:3128',
       '187.32.183.76:3128',
       '159.65.9.66:3128',
       '41.0.237.194:8080',
       '46.242.29.169:53281',
       '46.151.252.113:53281',
       '81.89.71.70:31222',
       '185.93.3.123:8080',
       '167.99.5.127:8080',
       '93.75.143.90:53281',
       '188.115.129.98:53281',
       '18.191.95.240:8080',
       '85.214.79.106:3128',
       '100.45.36.253:8080',
       '200.37.16.250:8080',
       '149.56.200.176:3128',
       '108.61.192.214:8080',
       '49.51.86.151:3128',
       '45.70.147.130:3128',
       '78.111.92.59:8080',
'153.122.51.17:8118',
'140.227.25.105:3128',
'94.25.131.55:8080',
'183.88.56.252:8080',
'176.108.47.38:3128',
'209.97.162.183:80',
'185.85.21.6:53281',
'121.46.95.27:8080',
'128.199.254.244:3128']
random.shuffle(tps)


#for i in range(1000):
    #foo.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+str(randint(100,999))+'.'+str(randint(10,99))+ '(KHTML, like Gecko) Chrome/66.0.'+str(randint(1000,9999))+'.'+str(randint(100,999)))

c = 10287
failed = open("failed", "wb")
p = 0
for title in titles:
    link = "https://api.ctext.org/gettext&urn=ctp:"+title
    filename = title.replace("/","+")
    headers = {'User-Agent': random.choice(foo)}
    source = []
    with requests.session() as r:
        r.keep_alive = False
        for _ in range(len(tps)):
            try:
                proxies = {'https': tps[p]}
                source = r.get(link, headers=headers, proxies=proxies, verify=False).text.splitlines()
            except ProxyError:
                tps.pop(p)
            else:
                break
        if len(source) == 0:
            random.shuffle(tps)
            p = 0
    #source = requests.get(link, headers=headers,proxies=proxies).text.splitlines()
    print(filename, len(source))

    while(len(source)==6 and "title" not in source[-2]):
        p+=1
        failed.write((title+"\n").encode('utf-8'))
        with requests.session() as r:
            r.keep_alive = False
            for _ in range(len(tps)):
                try:
                    proxies = {'https': tps[p]}
                    source = r.get(link, headers=headers, proxies=proxies, verify=False).text.splitlines()
                except ProxyError:
                    tps.pop(p)
                else:
                    break
            if len(source) == 6:
                random.shuffle(tps)
                p = 0

    file = open(str(c) + " " + filename + ".txt", "wb")
    for e in source[2:-3]:
        file.write((e+'\n').encode('utf-8'))
    file.close()
    c += 1
    #time.sleep(randint(0, 50)/1000)

