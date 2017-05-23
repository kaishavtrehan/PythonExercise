import re

fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	exit()
numlist=list()
for line in fhand:
	line=line.rstrip()
	x=re.findall('New .*: ([0-9].+)',line)
	if len(x)>0:
		numlist.append(float(x[0]))
		#print(x)
#print(numlist)
average=sum(numlist) / len(numlist)	
print('Average: ',average)
