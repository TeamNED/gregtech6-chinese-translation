# Load lang file
lang_path="C:\\Users\\Gordon's\\Documents\\GitHub\\gregtech6-chinese\\GregTech.lang"

with open(lang_path,'r') as original_file:
    original_data=original_file.read()

data=original_data.split('\n')
explaination={}

for line,index in zip(data,xrange(len(data))):
    if line.find('=')!=-1:
        explaination[str(index)]=line[line.find('=')+1:]

# Load Dictionary
dict_path=""

if dict_path:
    with open(dict_path,'r') as dictionary:
        dictionary_list=dictionary.read()
        dictionary_list=dictionary_dict.split('\n')

    dictionary_dict={}

    for line in dictionary_list:
        if line.find('=')!=0:
            dictionary_dict[dictionary_list[:line.find('=')]]=dictionary_list[line.find('=')+1:]

    del dictionary_list

    # Replacement
    for key in explaination.keys():
        context=explaination[key]
        for words in dictionary_dict.keys():
            if context.find(words)!=-1:
                context[context.find(words):context.find(words)+len(words)]
        explaination[key]=context

# Write file
output=""
for line,index in zip(data,xrange(len(data))):
    if explaination.has_key(str(index)):
        line=line.split('=')
        output+=line[0]+'='+explaination[str(index)]+'\n'
    else:
        output+=line+'\n'

destination_file=open('Gregtech_converted.lang','w+')
destination_file.write(output)
destination_file.close()