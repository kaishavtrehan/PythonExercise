import string

fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	exit()
counts=dict()
for line in fhand:
	line=line.rstrip()
	line=line.translate(string.punctuation)
	line=line.lower()
	#if line.find('From ') == -1:
	#	continue
	words=line.split()
	for word in words:
		filteredword=''.join(e for e in word if e.isalpha())
		t=tuple(filteredword)
		for letter in t:
			counts[letter]=counts.get(letter,0)+1
	#temp=words[5].split(':')
	#counts[temp[0]]=counts.get(temp[0],0)+1
lst=list()
for key,val in counts.items():
	lst.append((val,key))
#print('Before --->>> ', lst)
lst.sort(reverse=True)
#print('After --->>> ', lst)
for count,alpha in lst:
	print(alpha,count)
#print(counts)
