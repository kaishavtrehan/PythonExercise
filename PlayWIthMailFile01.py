fhand = open('mbox-short.txt')
emailList=list()
for line in fhand:
	line = line.rstrip()
	if line.find('From ') == -1 :
		continue
	words=line.split()
	for i in range(len(words)):
		if words[1] not in emailList :
			emailList.append(words[1])

for emailId in emailList:
	print(emailId + '\n')

print ('Email Id Count :- ' + str(len(emailList)))
	