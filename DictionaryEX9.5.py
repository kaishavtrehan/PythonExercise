fhand = open('mbox-short.txt')
emailList=dict()
for line in fhand:
	line = line.rstrip()
	if line.find('From ') == -1 :
		continue
	atpos=line.find('@')
	#print(atpos)
	sppos=line.find(' ',atpos)
	#print(sppos)
	host=line[atpos+1:sppos]
	emailList[host]=emailList.get(host,0)+1
print(emailList)	
	#words=line.split()
	#for word in words:
	#	emailList[words[1]]=emailList.get(words[1],0)+1

#lst=emailList.values()
#maxVal=max(lst)
#print(maxVal)
#maxVal=None
#for email in emailList:
#	if maxVal is None or  emailList[email] > maxVal :
#		maxVal=emailList[email]
#	print(maxVal, emailList[email])
#print('maxVal : ',maxVal)