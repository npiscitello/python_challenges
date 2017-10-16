#!/bin/python

import urllib.request
import pickle;
import sys;

url = "http://www.pythonchallenge.com/pc/def/banner.p";
unpacked = pickle.load(urllib.request.urlopen(url));

# iterate through the line lists
for i in unpacked:
    # iterate through the tuples in each line
    for j in i:
        # print the specified number of the specified character
        for k in range(0,j[1]):
            sys.stdout.write(j[0]);
    print();
