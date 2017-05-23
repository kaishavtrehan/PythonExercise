fname = input('Enter the file name: ')
try:
	fout = open(fname,'w')
except:
	print('File cannot be opened: ', fname)
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()