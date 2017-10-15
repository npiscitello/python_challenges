import xmlrpclib

server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
phonebook = xmlrpclib.Server(server_url)
methods = phonebook.system.listMethods()
for i in methods:
	print '\n'+str(i)+': '+str(phonebook.system.methodHelp(i))

print '\nsystem.phone(Bert): '+str(phonebook.phone('Bert'))

# SPOILER ALERT! The below line is for challenge 17! #










print '\nsystem.phone(Leopold): '+str(phonebook.phone('Leopold'))
