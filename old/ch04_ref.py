import urllib

string = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
print string.read()
