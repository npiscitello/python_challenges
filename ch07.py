from PIL import Image

image_path = 'oxygen.png'

im = Image.open(image_path).convert('RGB')

# find row with pixel values
for row in range(0, im.size[1] - 1):
	pix = im.getpixel((0,row))
	if pix[0] == pix[1] and pix[1] == pix[2]:
		break

print 'coded row: %d     ' % row,

# find average width of code blocks - stop when the code ends (no more grayscale)
length = 1 
lenlist = []
for column in range(1, im.size[0] - 1):
	pix = im.getpixel((column,row))
	if pix[0] != pix[1] or pix[1] != pix[2]:
		break
	if pix[0] == im.getpixel((column - 1, row))[0]:
		length += 1
	else:
		lenlist.append(length)
		length = 1

codewidth = int((sum(lenlist) / float(len(lenlist))) + 0.5)
print 'code width: %d' % codewidth

word = []
for letter in range(1, im.size[0] - 1, codewidth):
	pix = im.getpixel((letter, row))
	if pix[0] != pix[1] or pix[1] != pix[2]:
		break
	word.append(chr(pix[0]))

print 'raw: %r' % ''.join(word)

# extract list of numbers to convert
record = False
rawnumlist = []
for i in word:
	if i == '[':
		record = True
	if record and i != '[' and i != ']' and i != ',':
		rawnumlist.append(i)

# concatenate and convert numlist
j = 0
numlist = []
for i in range(2, len(rawnumlist), 4):
	numlist.append(rawnumlist[i - 2] + rawnumlist[i - 1] + rawnumlist[i])

for i in range(0, len(numlist)):
	numlist[i] = chr(int(numlist[i]))

print 'next keyword: %r' %  ''.join(numlist)
