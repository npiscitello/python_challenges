#!/bin/python

import urllib.request
import io;
import zipfile;

url = "http://www.pythonchallenge.com/pc/def/channel.zip";
zf = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url).read()), 'r', zipfile.ZIP_DEFLATED, True);

# uh oh is it a nothing thing like challenge 4?
