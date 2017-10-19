#!/bin/python

import urllib.request;
import re;
import bz2;

url = "http://www.pythonchallenge.com/pc/def/integrity.html";
source = urllib.request.urlopen(url).read().decode("utf-8");
username = re.search(r"^un: '(.*)'$", source, re.M)[1];
password = re.search(r"^pw: '(.*)'$", source, re.M)[1];

print(username);
# this prints EXACTLY RIGHT! It works if you dump what prints
# into a constant like bz2.decompress(b'print(username)');
# But when you try to convert it, extra backslashes get added......?

# How do we turn those escaped hex characters into bytes?
bz2.decompress(username);
