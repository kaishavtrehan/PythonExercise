import re
inputregex = input('Enter the regular expression: ')
fhand = open('m-box.txt')
count=0
for line in fhand:
	line=line.rstrip()
	if re.search(inputregex, line) :
		count=count+1
print('m-box.txt file has ',count,' has lines that matched ',inputregex)
