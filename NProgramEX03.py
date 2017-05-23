import urllib.request
import re
#from bs4 import BeautifulSoup

url = input('Enter - ')
source= urllib.request.urlopen(url)
print(type(source))
html = source.read().decode()
print(type(html))
#print(html)
#nonsecurelinks = re.findall('href="(http://.*?)"', html)
#securelinks = re.findall('href="(https://.*?)"', html)
#print(links)
#for nlink in nonsecurelinks:
#	print (nlink)
#print ('\n')	
#for slink in securelinks:
#	print (slink)