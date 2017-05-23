fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	exit()
countAddr=dict()
for line in fhand:
	line=line.rstrip()
	if line.find('From ') == -1:
		continue
	words=line.split()
	countAddr[words[1]]=countAddr.get(words[1],0)+1
	#print(words[1])
#print(countAddr)
lst=list()
for key,val in countAddr.items():
	lst.append((val,key))
lst.sort(reverse=True)
maxVal=max(lst)
print(maxVal)
#for val,key in lst:
	
#print(lst)		
#print('There were', count, 'subject lines in', fname)