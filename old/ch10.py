import re

# returns the next value in a See And Say sequence (1, 11, 21, 1211, 111221, etc...)
def seeAndSay(seed):
	tuples_list = []
	seedstr = str(seed)
	i = 0
	while True:
		# this is basically a showoff line, to avoid having to set variables.
		# it sets a tuple in the following form:
		# (number of the current digit in the string, current digit)
		search_result = ( len(re.search(seedstr[i]+'+',seedstr[i:]).group(0)), int(seedstr[i]) )
		tuples_list.append(search_result)
		i += search_result[0]
		if i == len(seedstr):
			break

	out_list = []
	for i in range(0, len(tuples_list)):
		out_list.append(str(tuples_list[i][0]))
		out_list.append(str(tuples_list[i][1]))

	return int(''.join(out_list))



num = 1
print '\nlen(a[0])  = %d' % num
for i in range(1,31):
	num = seeAndSay(num)
	if i < 10:
		print 'len(a[%d])  = %d' % (i, len(str(num)))
	else:
		print 'len(a[%d]) = %d' % (i, len(str(num)))

print '\nnext challenge url: http://www.pythonchallenge.com/pc/return/%d.html\n' % len(str(num))
