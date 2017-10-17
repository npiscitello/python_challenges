#!/bin/python

import urllib.request
import io;
import zipfile;
import re;
import sys;

url = "http://www.pythonchallenge.com/pc/def/channel.zip";
zf = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url).read()), 'r', zipfile.ZIP_DEFLATED, True);

nothing = 90052;
regex = re.compile(r"Next nothing is (\d*)$");
for i in range(0,len(zf.namelist()) - 1):
#    print("nothing " + "{0:03}".format(i) + " = " + str(nothing));
    sys.stdout.write(zf.getinfo(str(nothing)+".txt").comment.decode("utf-8"));
    try:
        nothing = int(re.search(regex, zf.open(str(nothing)+".txt").read().decode("utf-8"))[1]);
    except TypeError:
        break;

#print(zf.open(str(nothing)+".txt").read().decode("utf-8"));
