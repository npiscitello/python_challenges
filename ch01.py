def translate(input):
    word = list(input);
    for i in range(0, len(word)):
        if word[i] not in [' ', '.', '(', ')', "'"]:
            if word[i] == 'y':
                word[i] = 'a';
            elif word[i] == 'z':
                word[i] = 'b';
            else:	
                word[i] = chr(ord(word[i]) + 2);
    return ''.join(word);

print("\nHint string: " + 
        translate("G fmnc wms bgblr rpylqjyrc gr zw fylb. Rfyrq ufyr amknsrcpq ypc dmp. Bmgle gr "\
        "gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. Sqgle qrpgle.kyicrpylq() "\
        "gq pcamkkclbcb. Lmu ynnjw ml rfc spj."));
print("\nThe next challenge is: " + "".join(translate("map")) + '\n');
