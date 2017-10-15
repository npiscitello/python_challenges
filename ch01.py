#!/bin/python

import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/map.html";
source = urllib.request.urlopen(url).read();
# need double \\ escapes because the first '\\' escapes out of the string
# then the second '\\' escapes out of the regex.
code = re.match(".*<font color=\"#f000f0\">\\\\n(.*)\\\\n</tr></td>.*", str(source))[1];

def decode(code):
    decoded = [];
    for i in code:
        # we're only working in lowercase
        if( ord(i) >= 97 and ord(i) <= 122 ):
            # wraparound the alphabet
            if(ord(i) <= 120):
                decoded.append(chr(ord(i) + 2));
            else:
                decoded.append(chr(ord(i) - 24));
        elif( i != '\\' ):
            decoded.append(i);
    return "".join(decoded);

# this prints out the instructions to get the next url
#print(decode(code));

url_hint = re.match(".*/(.*)\\.html", url)[1];
print(decode(url_hint));
