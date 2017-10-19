#!/bin/python

import urllib.request;
import re;
import bz2;
import ast;

url = "http://www.pythonchallenge.com/pc/def/integrity.html";
source = urllib.request.urlopen(url).read().decode("utf-8");
username = re.search(r"^un: '(.*)'$", source, re.M)[1];
password = re.search(r"^pw: '(.*)'$", source, re.M)[1];

# rolling my own escape parser becasue Python sucks
# this converts "\x##" to an actual byte in the array
# it also deals with the random "\r" that's in there
# there has to be a way to do this natively - it's basically
# just parsing out backslash escape codes - but I couldn't
# figure out how to.
def parser(string):
    byte_string = bytearray();
    i = 0;
    while( i < len(string) ):
        if( string[i] == "\\" ):
            if( string[i+1] == "x" ):
                byte_string.append(int(string[i+2] + string[i+3], 16));
                i += 3;
            elif( string[i+1] == "r" ):
                byte_string.append(0x0D);
                i += 1;
        else:
            byte_string.append(ord(string[i]));
        i += 1;
    return byte_string;

print("un: " + bz2.decompress(parser(username)).decode("utf-8"));
print("pw: " + bz2.decompress(parser(password)).decode("utf-8"));
