#!/bin/python

import urllib.request
import codecs
import re

url = "http://www.pythonchallenge.com/pc/return/good.html";
auth = codecs.encode(b"huge:file", "base64").rstrip().decode("utf-8");
req = urllib.request.Request(url, None, {"Authorization": "Basic " + auth})
print(req.headers);
source = urllib.request.urlopen(req).read();
first = re.search(r"first:\n(.*)\n", str(source))[1];

print(first);
