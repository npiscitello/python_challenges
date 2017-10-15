#!/bin/python

import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html";
source = urllib.request.urlopen(url).read();
# The C programmer in me couldn't resist the one-liner... it's just stripping out the '\n's
code = "".join(re.search(r"<!--\\n(.*)\\n-->", str(source))[1].split(r"\n"));
# ...and this is finding all the specified groups
print("".join(re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", code)));
