import zipfile
import re
import time

namesuff = '.txt'
nothing = '90052'
order = [nothing]

# I would just import ch4.py, but there are differences between the two
# returns a string - either the nothing or text if a nothing isn't found
def findnothing():
	global string
	zipobject = zipfile.ZipFile('channel.zip', 'r')
	string = zipobject.open(str(nothing) + namesuff, 'r').read()
	matchObj = re.search(r'Next nothing is (\d+)', string, flags=0)
	if matchObj:
		print zipobject.getinfo(str(nothing) + namesuff).comment,
		return matchObj.group(1)
	else:
		return string

# iterate through all files (1001 to make sure we hit them all; not worried
#	about going too far because it breaks when it finds no nothing)
for i in range(0, 1001):
	try:
		nothing = int(findnothing())
	except ValueError:
		print '\nValueError! There is no nothing here!\n     String:\n%s' % findnothing()
		break

