import zipfile
import re
import time

namepre = 'channel/'
namesuff = '.txt'
nothing = '90052'
order = [nothing]

# I would just import ch4.py, but there are differences between the two
# returns a string - either the nothing or text if a nothing isn't found
def findnothing():
	global string
	string = open(namepre + str(nothing) + namesuff, 'r').read()
	matchObj = re.search(r'Next nothing is (\d+)', string, flags=0)
	if matchObj:
		return matchObj.group(1)
	else:
		return string

for i in range(0, 1001):
	try:
		nothing = int(findnothing())
		print 'Nothing %d = %d' % (i, nothing)
		order.append(nothing)
#		print 'String: %r' % string
	except ValueError:
		print '\nValueError! There is no nothing here!\n     String:\n%s' % findnothing()
		break
#	time.sleep(.1)

output = []
for i in range(0, len(order) - 1):
	output.append(zipfile.ZipFile('channel/channel.zip', 'r').getinfo(str(order[0]) + namesuff).comment)
print ''.join(output)
