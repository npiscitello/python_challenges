#!/bin/python

import re;

# look and say sequence
a = "1112231";
new_list = [];

# we know a sequence starting at one will never have a number greater than 3 in it
regex = re.compile(r"1*|2*|3*");

search = regex.search(a)[0];
new_list.append(str(len(search))); new_list.append(search[0]);

print(a);
print("".join(new_list));
