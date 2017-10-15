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
	for i in range(0, len(string)-1):
		try:
			nothinglist.append(str(int(string[i])))
		except ValueError:
			if nothing == 16044:
				divisor = 2
		if i == len(string) - 1 and nothinglist[0] == None:
			special = string
	nothing = int(''.join(nothinglist))/divisor
	if special != None:
		print "special: %r" % special
	return nothing

for i in range(0,400):
	print "nothing %d = %d" % (i, findnothing())
