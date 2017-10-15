import requests
import urllib
import re
import bz2

# set variables
cookie_file = "ch17_cookies"
urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
busynothing=12345
cookiedata = []

# function from challenge 4 to find the next nothing
def findNextNothing(nothing):
	response = requests.get(urlbase+str(nothing))
	matchObj = re.search(r'next busynothing is (\d+)', response.text)
	if matchObj:
		return [int(matchObj.group(1)), response.cookies['info']]
	else:
		return[None, response.cookies['info']]

# get every nothing and cookie value
for i in range(0,125):
	result = findNextNothing(busynothing)
	cookiedata.append(result[1])
	print "busynothing: %d, cookie data: %r" % (busynothing,cookiedata[i])
	if result[0] is None:
		break
	else:
		busynothing = result[0]

# decode the cookie values (percent encoded BZ2 compressed data)
string = urllib.unquote(''.join(cookiedata).replace('+', '%20'))
string = bz2.decompress(string)
print string
print '\n\n'

# after some research... yeah, I cheated, deal with it. #

# extract the target string
matchObj = re.search(r'.*"(.*)".*', string)
# send the correct cookie and display the output
if matchObj:
	string = matchObj.group(1).replace(' ', '+')
	cookie = {'info': string}
	print requests.post("http://www.pythonchallenge.com/pc/stuff/violin.php", cookies=cookie).text
