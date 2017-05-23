import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n'.encode(encoding='UTF-8'))

count = 0
picture = "";
while True:
	#print('RAW----- ',type(mysock.recv(5120)))
	data = mysock.recv(5120)
	#print(type(data))
	if ( len(data) < 1 ) : break
	# time.sleep(0.25)
	count = count + len(data)
	#print (len(data),count)
	picture = picture + data.decode(encoding='iso-8859-1')
mysock.close()
# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n");
#print ('Header length',pos)
print (picture[:pos+4])
# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")
fhand.write(picture.encode(encoding='iso-8859-1'))
fhand.close()