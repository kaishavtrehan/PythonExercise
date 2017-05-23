import string
fhand=open('romeofull.txt')
counts=dict()
for line in fhand:
	line=line.rstrip()
	line=line.translate(string.punctuation)
	line=line.lower()
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1
	#print(counts)
#Sort Dictionary by values
lst=list()
for key, val in counts.items():
	lst.append( (val, key) )
	#print(key,val,counts[key])
#print(lst)
lst.sort(reverse=True)
for val, key in lst[:50] : #slicing a list
	print (key, val)