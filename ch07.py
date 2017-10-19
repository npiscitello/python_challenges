#!/bin/python

import urllib.request
from PIL import Image
import sys;
import re;

url = "http://www.pythonchallenge.com/pc/def/oxygen.png";
img = Image.open(urllib.request.urlopen(url));
# empirically determined:
#   - row 47 is the middle of the greyscale strip
#   - greyscale block dimensions are 7px wide by 9px tall
ROW = 47;
WIDTH = 7;

outstring = "";
for i in range(0, img.size[0], WIDTH):
    outstring += chr(img.getpixel((i, ROW))[0]);

next_url = re.search(r"\[(.*)\]", outstring)[1];

for i in next_url.split(", "):
    sys.stdout.write(chr(int(i)));
print();
