import urllib
import re

url = raw_input("enter the web link")
p= urllib.urlopen(url)
a = p.read()

pattern = re.compile('img src=[ "](.*?)"' )
a = re.findall(pattern , a)

f=open("new.txt","w")

for i in a:

		f.write(url + i+ "\n")


f.close()