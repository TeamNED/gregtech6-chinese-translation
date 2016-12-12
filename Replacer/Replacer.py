# Load lang file
lang_path="GregTech.lang"

with open(lang_path,'r') as original_file:
    original_data=original_file.read()

data=original_data.split('\n')
explaination={}

for line,index in zip(data,xrange(len(data))):
    if line.find('=')!=-1:
        explaination[str(index)]=line[line.find('=')+1:]

# Load Dictionary
dict_path="dictionary.dict"

if dict_path:
    with open(dict_path,'r') as dictionary:
        dictionary_list=dictionary.read()
        dictionary_list=dictionary_list.split('\n')

    dictionary_dict={}

    for line in dictionary_list:
        if line.find('=')!=0 and line.find('=')!=len(line)-1:
            dictionary_dict[line[:line.find('=')]]=unicode(line[line.find('=')+1:],'gb2312')

    del dictionary_list

    # Replacement
    for key in explaination.keys():
        context=explaination[key]
        for words in dictionary_dict.keys():
            if context.find(words)!=-1:
                temp=context[:context.find(words)]
                temp+=dictionary_dict[words]
                temp+=context[context.find(words)+len(words):]
                context=temp
        if not isinstance(context,unicode):
            explaination[key]=unicode(context,'gb2312')
        else:
            explaination[key]=context

# Write file
output=unicode("",'gb2312')
for line,index in zip(data,xrange(len(data))):
    if explaination.has_key(str(index)):
        line=line.split('=')
        output+=unicode(line[0],'gb2312')+'='+explaination[str(index)]+'\n'
    else:
        output+=line+'\n'

destination_file=open('Gregtech_converted.lang','w+')
destination_file.write(output.encode('utf8'))
destination_file.close()