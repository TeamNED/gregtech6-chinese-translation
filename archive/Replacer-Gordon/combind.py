translation=open("C:\\Users\\Gordon\\Documents\\GitHub\\gregtech6-chinese\\Replacer\\a.txt","r")
translation=translation.read()
translation=translation.split('\n')
original=open("C:\\Users\\Gordon\\Documents\\GitHub\\gregtech6-chinese\\Replacer\\pending_dictionary.txt",'r')
original=original.read()
original=original.split('\n')
output=unicode("",'gb2312')
for a,b,index in zip(original,translation,range(len(original))):
	output+=unicode(a,'gb2312')+unicode("=",'gb2312')+unicode(b,'gb2312')+"\n"
file=open('output_dictionary.txt','w')
file.write(output.encode("utf-8"))
file.close()

