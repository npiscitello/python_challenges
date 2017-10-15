import gzip
from PIL import Image
import difflib

src_path = "deltas.gz"
src = gzip.open(src_path)

# calculate the diff between the two; the first line is a PNG file header?
# first 53 characters are first line, rest are second line (55-108)

raw = src.read()
str1 = ""
str2 = ""
index = 0
for i in raw:
	if index >= 0 and index <= 53:
		str1 += i
	elif index >= 55 and index <=108:
		str2 += i
	index += 1
	if i == '\n':
		str1 += i
		str2 += i
		index = 0

diff = list(difflib.Differ().compare(str1.splitlines()[0:10],str2.splitlines()[0:10]))
print diff
