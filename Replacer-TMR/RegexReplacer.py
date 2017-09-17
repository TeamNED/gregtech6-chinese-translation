# GT6-Translation RegexReplacer.py
# by Tanimodori CC-BY-NC-SA 4.0

import sys
import codecs
import re
import os.path
import json
import argparse
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())  # utf-8 output

# Paths

parser = argparse.ArgumentParser(
    description='A simple regex-based replacer dealt with GregTech6 Chinese Translasion')
parser.add_argument(
    'translated', help='Filepath of currently translated GregTech.lang')
parser.add_argument('original', help='Filepath of oringinal GregTech.lang')
parser.add_argument(
    'glossary', help='Filepath of glossary, auto-create if not exist')
parser.add_argument('pattern', help='Filepath of regex patterns')
parser.add_argument('output', help='Filepath of output GregTech.lang')
args = parser.parse_args()

TranslatedPath = args.translated
OriginalPath = args.original
OutputPath = args.output
GlossaryPath = args.glossary
PatternPath = args.pattern

# Settings

# To delete item only exist in translated file - Must be False
DeleteObsoleteItem = False
# To Use translated translations instead of the processed ones
RespectTranslated = False
AllowPartlyTranslation = False      # To allow unknown mainWord in translation
LearnGlossary = True                # To learn Glossary


class langFile:
    def __init__(self, data):
        self.data = data

    @classmethod
    def loadFile(cls, path):
        result = langFile({})
        with open(path, 'r', encoding='utf-8') as f:
            for l in f:
                l = l.strip()
                if l.startswith('S:'):
                    i = l.index('=')
                    result.data[l[2:i]] = l[i + 1:]
        return result

    def save(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(
                '# Configuration file\r\n\r\nenablelangfile {\r\n    B:UseThisFileAsLanguageFile=true\r\n}\r\n\r\n\r\nlanguagefile {\r\n')
            for item in sorted(self.data.items(), key=lambda x: x[0]):
                f.write('    S:{0}={1}\r\n'.format(item[0], item[1]))
            f.write('}\r\n\r\n\r\n')


class pattern:
    glossary = {}
    instances = []

    def __init__(self, nameRegex, valueRegex, repl, priority=-1):
        self.nameString = nameRegex
        self.nameRegex = re.compile(nameRegex)
        self.valueString = valueRegex
        self.valueRegex = re.compile(valueRegex)
        self.repl = repl
        self.replRegex = re.compile(repl.replace('\\1', '(.+)'))
        self.priority = priority
        pattern.instances.append(self)

    @classmethod
    def process(cls, item, translated):
        currentTranslation = item[1]
        originalTranslation = item[1]
        processPatterns = sorted(filter(lambda x: x.nameRegex.match(
            item[0]) is not None, pattern.instances), key=lambda x: x.priority, reverse=True)
        if len(processPatterns) > 0:
            mainWord = ''
            if LearnGlossary:
                if translated is None:
                    canLearnGlossary = False
                else:
                    mainWordTranslated = translated
                    canLearnGlossary = True

            for p in processPatterns:
                ma = p.valueRegex.match(currentTranslation)
                if ma is None:
                    continue  # No match
                mainWord = ma.group(1).strip()
                if LearnGlossary and canLearnGlossary:
                    ma2 = p.replRegex.match(mainWordTranslated)
                    if ma2 is None:
                        canLearnGlossary = False
                    else:
                        mainWordTranslated = ma2.group(1).strip()
                currentTranslation = re.sub(
                    p.valueRegex, p.repl, currentTranslation)
            if mainWord != '':
                # succ
                if mainWord in pattern.glossary:
                    return currentTranslation.replace(mainWord, pattern.getMainWord(item[0], mainWord))
                else:
                    if canLearnGlossary and mainWordTranslated != mainWord:
                        pattern.glossary[mainWord] = mainWordTranslated
                        return currentTranslation.replace(mainWord, pattern.glossary[mainWord])
                    if AllowPartlyTranslation:
                        # Partly Translate
                        return currentTranslation
                    elif translated is not None:
                        # No Partly Translation, use translated
                        return translated
                    else:
                        # Neither Partly nor translated, use original
                        return originalTranslation
        # fail
        # if item[1] in pattern.glossary:
        #    return pattern.glossary[item[1]]
        # elif translated is None:
        if translated is None:
            # No available translation
            return originalTranslation
        else:
            # Use current translation
            return translated

    @classmethod
    def getMainWord(cls, name, word):
        if word not in pattern.glossary:
            return None
        obj = pattern.glossary[word]
        if type(obj) is str:
            return obj
        else:
            fallback = None
            for k, v in obj.items():
                if k == '.*':
                    fallback = v
                    continue
                if re.match(k, name):
                    return v
            return fallback

    #@classmethod
    # def cleanupGlossary(cls):

    @classmethod
    def loadFile(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            arr = json.loads(f.read())
            if len(arr) > 0:
                for item in arr:
                    pattern(item['name'], item['value'],
                            item['repl'], item['priority'])


if __name__ == '__main__':
    # Load File
    _ori = langFile.loadFile(OriginalPath)
    _old = langFile.loadFile(TranslatedPath)
    _new = langFile({})
    pattern.loadFile(PatternPath)
    if os.path.isfile(GlossaryPath):
        try:
            with open(GlossaryPath, 'r', encoding='utf-8') as f:
                pattern.glossary = json.load(f)
        except:
            pattern.glossary = {}
            with open(GlossaryPath, 'w', encoding='utf-8') as f:
                f.write("{}\r\n")
    else:
        with open(GlossaryPath, 'w', encoding='utf-8') as f:
            f.write("{}\r\n")

    # Replacement
    _sortedOri = sorted(_ori.data.items(), key=lambda x: x[0])
    _sortedOld = sorted(_old.data.items(), key=lambda x: x[0])
    cnt = 0
    for item in _sortedOri:
        while item[0] > _sortedOld[cnt][0]:
            # Obsolete item or unknown mod
            if not DeleteObsoleteItem:
                _new.data[_sortedOld[cnt][0]] = _sortedOld[cnt][1]
            cnt += 1
        if item[0] < _sortedOld[cnt][0]:
            # New entry, try to process
            processed = pattern.process(item, None)
            _new.data[item[0]] = processed
        else:
            # elif item[0]=_sortedOld[cnt][0]:
            # Have live translation
            if RespectTranslated:
                _new.data[item[0]] = _sortedOld[cnt][1]
            else:
                processed = pattern.process(item, _sortedOld[cnt][1])
                _new.data[item[0]] = processed
            cnt += 1

    _new.save(OutputPath)
    with open(GlossaryPath, 'w', encoding='utf-8') as f:
        json.dump(pattern.glossary, f, ensure_ascii=False,
                  sort_keys=True, indent=4)
