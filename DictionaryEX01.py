word = 'brontosaurus'
d = dict()
print(word)
for c in word:
	d[c] = d.get(c,0) + 1
	#if c not in d:
	#	d[c] = 1
	#else:
	#	d[c] = d[c] + 1
print(d)