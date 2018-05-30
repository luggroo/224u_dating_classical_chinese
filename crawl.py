import codecs
import re

f = codecs.open('Chinese Text Project.html', encoding='utf-8')
lines = []
file = open("booktitles.txt","wb")
for line in f:
    if ("class=\"sprite-expand\" title=\"+\">+<div style=\"display: inline;\"></div></a></div><a" in line):
        a = re.findall(r'href=\"([^\"]*?)\">([^<]*?)</a>', line)
        print(a)
        uni = (a[0][0]+" , "+a[0][1]+"\n").encode('utf-8')
        print(uni)
        file.write(uni)


