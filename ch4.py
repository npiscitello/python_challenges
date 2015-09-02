import urllib
import re

# pseudocode
# get html
# search for next nothing
#	regex "next nothing is "
# use nothing to get next nothing
# if no match and nothing 16044, divide by 2
# if no match and anything else, print text




urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = 12345
divisor = 1
string = None
def findnothing():
	global nothing; global divisor; global string
	string = urllib.urlopen(urlbase+str(nothing)).read()
	matchObj = re.search(r'next nothing is (\d+)', string, flags=0)
	if matchObj:
		nothing = int(matchObj.group(1))
	elif nothing == 16044:
		nothing /= 2
#		divisor = 2
	nothing /= divisor
	return nothing

for i in range(0, 401):
	print "nothing %d = %d     string = %s" % (i, findnothing(), string)
