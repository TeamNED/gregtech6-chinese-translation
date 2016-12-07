# Load unfinished lang file
file_path="GregTech.lang"

with open(file_path,'r') as original_file:
    original_data=original_file.read()

data=original_data.split('\n')
explaination={}

for line,index in zip(data,xrange(len(data))):
    if line.find('=')!=-1:
        explaination[str(index)]=line[line.find('=')+1:]

# Count untranslated words
words={}
for key in explaination.keys():
    context=explaination[key]
    context=context.split(" ")
    for word in context:
        if words.has_key(word):
            words[word]+=1
        else:
            words[word]=1
print words
# Write to file
output=""
for key in words.keys():
    output+=key
    output+="=\n"

destination_file=open('pending_dictionary.dict','w+')
destination_file.write(output)
destination_file.close()