fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	exit()
counts=dict()
for line in fhand:
	line=line.rstrip()
	if line.find('From ') == -1:
		continue
	words=line.split()
	temp=words[5].split(':')
	counts[temp[0]]=counts.get(temp[0],0)+1
lst=list()
for key,val in counts.items():
	lst.append((key,val))
#print('Before --->>> ', lst)
lst.sort(reverse=False)
#print('After --->>> ', lst)
for hour,count in lst:
	print(hour,count)
