import urllib.request
import re
from bs4 import BeautifulSoup

url = input('Enter - ')
source= urllib.request.urlopen(url)
html = source.read().decode()
#print(html)
soup=BeautifulSoup(html,"html.parser")
tags=soup('a')
#links = re.findall('href="(http://.*?)"', html)
#print(links)
for tag in tags:
	print (tag.get('href',None))
	# Look at the parts of a tag
	print ('TAG:',tag)
	print ('URL:',tag.get('href', None))
	print ('Content:',tag.contents[0])
	print ('Attrs:',tag.attrs)