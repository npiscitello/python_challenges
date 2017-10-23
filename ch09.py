#!/bin/python

import urllib.request
import codecs
import re
from PIL import Image
from PIL import ImageDraw

url = "http://www.pythonchallenge.com/pc/return/good.html";
auth = codecs.encode(b"huge:file", "base64").rstrip().decode("utf-8");
req = urllib.request.Request(url, None, {"Authorization": "Basic " + auth})
source = urllib.request.urlopen(req).read().decode("utf-8");
data = [];
data.append("".join(re.search(r"first:\n(.*?)\n\n", source, re.DOTALL)[1].split("\n")).split(","));
data.append("".join(re.search(r"second:\n(.*?)\n\n", source, re.DOTALL)[1].split("\n")).split(","));

# create point tuples
line = [];
width = 0; height = 0;
for i in range(0, len(data)):
    line.append([]);
    for j in range(0, len(data[i]), 2):
        if( int(data[i][j+0]) > width  ): width  = int(data[i][j+0]);
        if( int(data[i][j+1]) > height ): height = int(data[i][j+1]);
        line[i].append((int(data[i][j+0]), int(data[i][j+1])));

im = Image.new("1", (width + 10, height + 10), 1);
draw = ImageDraw.Draw(im);
for i in line:
    draw.line(i, 0, 1);

outfile = "ch09.png";
im.save(outfile);
print("Solution saved in " + outfile);
