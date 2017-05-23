import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	
	#x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
	#if len(x) > 0 :
	#	print (x)
	
	#if re.search('^From:.+@', line) :
	#	print (line)
	
	#if re.search('X-.*: [0-9.]+', line) :
	#	print(line)
	
	#x = re.findall('X-.*: ([0-9.]+)', line)
	#if len(x) > 0 :
	#	print (x)
		
	#x = re.findall('Details:.*rev=([0-9.]+)', line)
	#if len(x) > 0 :
	#	print (x)
	
	x = re.findall('From.* ([0-9][0-9]):', line)
	if len(x) > 0 :
		print (x, line)