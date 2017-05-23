fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	exit()
wordlist=list()	
for line in fhand:
	line = line.rstrip()
	words=line.split()
	for i in words:
		if i not in wordlist:	
			wordlist.append(i)
wordlist.sort()
print(wordlist)	