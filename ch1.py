def translate(input):
	word = list(input)
	i = 0
	for j in word:
		if j == 'k':
			word[i] = 'm'
		elif j == 'm':
			word[i] = 'k'
		elif j == 'o':
			word[i] = 'q'
		elif j == 'q':
			word[i] = 'o'
		elif j == 'e':
			word[i] = 'g'
		elif j == 'g':
			word[i] = 'e'
		i += 1
	return word

list = translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
string = ''.join(list)
print string
