def translate(input):
	word = list(input)
	for i in range(0, len(word) - 1):
		if word[i] not in [' ', '.', '(', ')', "'"]:
			if word[i] == 'y':
				word[i] = 'a'
			elif word[i] == 'z':
				word[i] = 'b'
			else:	
				word[i] = chr(ord(word[i]) + 2)
	return word

list = translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
string = ''.join(list)
print string
