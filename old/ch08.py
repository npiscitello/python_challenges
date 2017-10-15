import bz2
import urllib
import re

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
string = urllib.urlopen(url).read()

# use this to find strings
unObj = re.search(r"un: '(.+)'", string)
pwObj = re.search(r"pw: '(.+)'", string, flags=0)

if unObj and pwObj:
	login = []
	for i in (unObj.group(1), pwObj.group(1)):
		login.append(bz2.decompress(i.decode('string_escape')))

	print '\nusername: %s\npassword: %s\n' % (login[0], login[1])
else:
	print 'no matches!'
