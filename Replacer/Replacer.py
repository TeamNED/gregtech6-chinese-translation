# Load lang file
lang_path="GregTech.lang"

with open(lang_path,'r') as original_file:
    original_data=original_file.read()

original_data=original_data.decode("utf-8")
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
        dictionary_list=dictionary_list.decode("utf-8")
        dictionary_list=dictionary_list.split('\n')

    dictionary_dict={}

    for line in dictionary_list:
        if line.find('=')!=0 and line.find('=')!=len(line)-1:
            dictionary_dict[line[:line.find('=')]]=line[line.find('=')+1:]

    del dictionary_list

    # Replacement
    for key in explaination.keys():
        context=explaination[key]
        context=context.split()
        for original_words,index in zip(context,range(len(context))):
            for words in dictionary_dict.keys():
                if original_words.lower()==words.lower():
                    context[index]=dictionary_dict[words]
        explaination[key]=' '.join(context)

# Write file
output=""
for line,index in zip(data,xrange(len(data))):
    if explaination.has_key(str(index)):
        line=line.split('=')
        output+=line[0]+'='+explaination[str(index)]+'\n'
    else:
        output+=line+'\n'

destination_file=open('Gregtech_converted.lang','w+')
destination_file.write(output.encode('utf-8'))
destination_file.close()
