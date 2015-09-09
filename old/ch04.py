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
nothing_init = 12345

def findNextNothing(nothing):
	string = urllib.urlopen(urlbase+str(nothing)).read()
	matchObj = re.search(r'next nothing is (\d+)', string) 
	if matchObj:
		return [int(matchObj.group(1)), string, False]
	elif re.search(r'Divide by two', string):
		return [nothing/2, string, False]
	elif re.search(r'.+html', string):
		return [nothing, string, True]

result = [nothing_init]
for i in range(0, 401):
	result = findNextNothing(result[0])
	print "nothing %d = %d     string = %s" % (i, result[0], result[1])
	if result[2]:
		break
