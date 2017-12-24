# gregtech6-chinese-translate
GregTech6汉化项目，欢迎加入。

当前适配版本为v6.06.03

原始文件源自Amamiya组,感谢Tanimodori的更新与对一堆奇葩问题的修复

## Notes from Gordon
I'm so buzy these days, so i may update it after I've done all works >_<

## Current Works:
  - Translate all english description into Chinese
  - Make the translations make sense
  - Sleep :P (I like sleeping!!My heaven!!)

## How we change it?
  - Ind: Stupidly replace all words :P (Just kidding~)
  - Gordon: Based on these two regular expression:
    - [^\=\.\(\-\:]\b"Search_context" --> Find target contexts the first word after "="
    - =\b"Search_context" --> Find target contexts right after "="
    - Just created a script that can based on the translation of words to words (Maybe weird, but IDC! xD)
  - NH4HCr2O7:As the playtester I guarantee that THE STUPID METHOD IS USEFUL SOMETIMES
  - Tanimodori: Using Replacer-TMR:
    - Update glossary.json and/or patterns.json
    - $ python3 Replacer-TMR/RegexReplacer.py GregTech.lang Original/GregTech.lang Replacer-TMR/glossary.json Replacer-TMR/patterns.json GregTech.lang

## license
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />本汉化项目 采用 <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a>进行许可。


### if you have any question, please post it in issues
