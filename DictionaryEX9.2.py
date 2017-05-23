fhand = open('mbox-short.txt')
days=dict()
for line in fhand:
	line = line.rstrip()
	if line.find('From ') == -1 :
		continue
	words=line.split()
	#print(words)
	for word in words:
		#print(words[2])
		#if words[2] in words:
			#print(word)
			days[words[2]]=days.get(words[2],0)+1
print(days)
#for day in dayList:
#	print(day + '\n')