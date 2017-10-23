#!/bin/python

import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/return/good.html";
source = urllib.request.urlopen(url).read();
first = re.search(r"first:\n(.*)\n\n", str(source))[1];

print(first);
