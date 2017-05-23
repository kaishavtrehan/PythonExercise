fhand = open('mbox-short.txt')
emailList=dict()
for line in fhand:
	line = line.rstrip()
	if line.find('From ') == -1 :
		continue
	words=line.split()
	#print(words)
	for word in words:
		emailList[words[1]]=emailList.get(words[1],0)+1

#lst=emailList.values()
#maxVal=max(lst)
#print(maxVal)
maxVal=None
for email in emailList:
	if maxVal is None or  emailList[email] > maxVal :
		maxVal=emailList[email]
	print(maxVal, emailList[email])
print('maxVal : ',maxVal)