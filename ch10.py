#!/bin/python

import re;

# look and say sequence
a = "1";
new_list = [];
last_match_index = 0;

# we know a sequence starting at one will never have a number greater than 3 in it
# I'm sure there's a way to make this regex more general, but it's late and it works
regex = re.compile(r"1{1,3}|2{1,3}|3{1,3}");

for i in range(0,30):
    last_match_index = 0;
    match = regex.match(a[last_match_index:]);
    while match:
        last_match_index += match.end(0);
        new_list.append(str(len(match[0]))); new_list.append(match[0][0]);
        match = regex.match(a[last_match_index:]);
    a = "".join(new_list);
    new_list.clear();

print(len(a));
