fahrenheit  = input('Enter Temp in fahrenheit : ')
try:
	fahrenheit  = int(fahrenheit )
	celcius = (fahrenheit - 32) * 5/9
	print (celcius)
except:
	print ('Enter a valid number')
