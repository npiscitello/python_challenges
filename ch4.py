import urllib

urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = 12345
divisor = 1
def findnothing():
	global nothing; global divisor
	nothinglist = []
	num = None
	special = None
	raw = urllib.urlopen(urlbase+str(nothing))
	string = raw.read()
	for i in string:
		try:
			nothinglist.append(str(int(i)))
		except ValueError:
			if nothing == 16044:
				nothinglist = ['8', '0', '2', '2']
				divisor = 2
			elif divisor == 2:
				special = string
	nothing = int(''.join(nothinglist))/divisor
	if special != None:
		print "special: %r" % special
	return nothing

for i in range(0,400):
	print "nothing %d = %d" % (i, findnothing())
