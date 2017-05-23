fhand = open('m-box.txt')
count=0
for line in fhand:
	if line.startswith('From:') :
		line = line.rstrip()
		count=count+1
		tempLine='Line# %d -> %s' % (count,line)
		print(tempLine) 
		if count==99 :
			break