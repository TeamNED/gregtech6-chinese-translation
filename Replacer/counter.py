class counter():
    def __init__(self):
        import string
        self.string=string
        self.CountWords_return={}
    def LoadLangFile(self):
        '''Load unfinished lang file'''
        file_path="GregTech.lang"

        with open(file_path,'r') as original_file:
            original_data=original_file.read()

        return original_data
    def ExtractExplaination(self,original_data):
        data=original_data.split('\n')
        explaination={}

        for line,index in zip(data,xrange(len(data))):
            if line.find('=')!=-1:
                explaination[str(index)]=line[line.find('=')+1:]

        return explaination
    def CountWords(self,explaination,multithread=False,threadLock=None):
        '''Count untranslated words'''
        words={}
        punctuation=[x for x in self.string.punctuation]
        for key in explaination.keys():
            context=explaination[key]
            context=context.split(" ")
            for word in context:
                word=word.replace('<BR>','')
                letters=[x for x in word]
                # Inverse
                for letter,index in zip(letters,xrange(len(letters))):
                    Is_punctuation=False
                    for punc in punctuation:
                        if letter==punc:
                            del letters[index]
                            Is_punctuation=True
                            break
                        elif letter!=punc:
                            pass
                    if not Is_punctuation:
                        break
                    elif Is_punctuation:
                        pass
                # Reverse
                for letter,index in zip(letters[::-1],[y for y in xrange(len(letters))][::-1]):
                    Is_punctuation=False
                    for punc in punctuation:
                        if letter==punc:
                            del letters[index]
                            Is_punctuation=True
                            break
                        elif letter!=punc:
                            pass
                    if not Is_punctuation:
                        break
                    elif Is_punctuation:
                        pass

                word=''.join(letters)

                if words.has_key(word):
                    words[word]+=1
                elif self.CountWords_return.has_key(word) and multithread==True:
                    threadLock.acquire()
                    self.CountWords_return[word]+=1
                    threadLock.release()
                elif not self.CountWords_return.has_key(word) and multithread==True:
                    threadLock.acquire()
                    self.CountWords_return[word]=1
                    threadLock.release()
                else:
                    words[word]=1
        return words
    def WriteResult(self,words):
        '''Write to file'''
        output=""
        for key in words.keys():
            output+=key
            output+="=\n"

        destination_file=open('pending_dictionary.dict','w+')
        destination_file.write(output)
        destination_file.close()
    def MultiTasking(self,threadAmount=2):
        original_data=self.LoadLangFile()
        explaination=self.ExtractExplaination(original_data)
        explaination_length=len(explaination.keys())
        explaination_keys=explaination.keys()
        slice_size=explaination_length/threadAmount
        # Create Threads
        import threading
        self.threadLock=threading.Lock()
        thread_instance=[]
        for thread in range(1,threadAmount+1):
            if thread==threadAmount:
                task=[]
                for items in range(slice_size*(threadAmount-1),explaination_length):
                    task.append(explaination_keys[items])
                job={}
                for line_index in task:
                    job[str(line_index)]=explaination[str(line_index)]
                instance=threading.Thread(target=self.CountWords,args=(job,),kwargs={'multithread':True,'threadLock':self.threadLock})
                instance.start()
                thread_instance.append(instance)
            else:
                task=[]
                for items in range(slice_size*(thread-1),slice_size*thread):
                    task.append(explaination_keys[items])
                job={}
                for line_index in task:
                    job[str(line_index)]=explaination[str(line_index)]
                instance=threading.Thread(target=self.CountWords,args=(job,),kwargs={'multithread':True,'threadLock':self.threadLock})
                instance.start()
                thread_instance.append(instance)
        for thread in thread_instance:
            thread.join()
        words=self.CountWords_return
        self.WriteResult(words)


if __name__=='__main__':
    instance=counter()
    original_data=instance.LoadLangFile()
    explaination=instance.ExtractExplaination(original_data)
    words=instance.CountWords(explaination,False)
    instance.WriteResult(words)
