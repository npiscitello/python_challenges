#!/bin/python

import urllib.request
import re

# yeah, I'm not parsing out the original source for the first nothing.
# sue me.
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";
source = "";
nothing = "12345";

for i in range(0,400):
    # special cases given as instructions from pythonchallenge.com
    if( int(nothing) == 16044 ):
        nothing = str(int(int(nothing) / 2));

    print("nothing " + "{0:03}".format(i) + " = " + nothing);
    source = urllib.request.urlopen(base_url+nothing).read().decode("utf-8");

    if( int(nothing) == 66831 ):
        break;

    nothing = re.search(r"and the next nothing is (\d*)", str(source))[1];

print("\n" + urllib.request.urlopen(base_url+nothing).read().decode("utf-8"));
