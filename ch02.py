#!/bin/python

import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html";
source = urllib.request.urlopen(url).read();
# need double \\ escapes because the first '\\' escapes out of the string
# then the second '\\' escapes out of the regex.
code = re.match(".*<!--\\\\n(.*)\\\\n-->.*", str(source))[1];

# ignore newlines; we're assuming there are no significant '\s' or 'n's
freq_dict = {};
for i in code:
    if( i != '\\' and i != 'n' ):
        if( i in freq_dict ):
            freq_dict[i] += 1;
        else:
            freq_dict[i] = 1;

# turns out, there are a few characters that only occur once
del_from_dict = [];
for i in freq_dict:
    if( freq_dict[i] != 1 ):
        del_from_dict.append(i);

for i in del_from_dict:
    del freq_dict[i];

print("".join(freq_dict));
