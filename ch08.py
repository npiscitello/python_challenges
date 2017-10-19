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
# how do I get Python to interpret the '\xXX' as an escape sequence
# instead of actual characters?

# How do we turn those escaped hex characters into bytes?
bz2.decompress(username);
