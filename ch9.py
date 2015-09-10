import re
from PIL import Image,ImageDraw

path = 'ch9_source'
raw = open(path, 'r').read()

searchObj = re.search(r'first:\s(.+)\s\ssecond:\s(.+)\s\s-->', raw, flags=re.DOTALL)

raw = [None, None]
raw[0] = searchObj.group(1)
raw[1] = searchObj.group(2)

# do for loop: add to current index until comma; comma increments
data_list = [[],[]]
for i in range(0,len(data_list)):
	x = 0
	for j in raw[i]:
		if j == ',':
			x += 1
		elif j == '\n':
			pass
		else:
			try:
				data_list[i][x] += j
			except IndexError:
				data_list[i].append(j)

for i in range(0,len(data_list)):
	for j in range (0,len(data_list[i])):
		data_list[i][j] = int(data_list[i][j])

if max(data_list[0]) > max(data_list[1]):
	size = max(data_list[0])
else:
	size = max(data_list[1])

im = Image.new('1', (size,size), 1)
draw = ImageDraw.Draw(im)
draw.line(data_list[0])
draw.line(data_list[1])
im.save('first+second.png')
