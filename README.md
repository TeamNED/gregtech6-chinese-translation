# gregtech6-chinese-translation
![Translation status big](https://weblate.sayori.pw/widgets/gregtech/zh_cn/gregtech6/287x66-grey.png)

![Translation Status](https://weblate.sayori.pw/widgets/gregtech/-/svg-badge.svg) ![Build Status](https://travis-ci.org/MoHaDouBiTeam/gregtech6-chinese-translation.svg?branch=master)

[最新版(Nightly Build)汉化文件下载地址](https://github.com/MoHaDouBiTeam/gregtech6-chinese-translation/blob/master/GregTech.lang)

[Weblate翻译服务器](https://weblate.sayori.pw/engage/gregtech/?utm_source=widget)

GregTech6汉化项目，欢迎加入。

当前适配版本为v6.07.04，内置兼容QwerTech-1.0.0-a.21

原始文件源自Amamiya组

## Notes from Gordon
I'm so buzy these days, so i may update it after I've done all works >_<

## Current Works:
  - Translate all English description into Chinese
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

## 工作流程指南:善用Project
在某次更新后，GitHub给了我们一个强大的工具，就是Project。它并不只是个卡片墙，而是集成了自动Issues/PR归类收集形成Todo List和Todo List完成程度统计的自动化工程管理工具。

~~废话毕~~。我们来看下具体怎么用。我把Projects页面分成了三份，*任务队列，已完成，讨论中。*
- 任务队列：已经讨论完毕，只缺动手的任务。
- 讨论中：还在撕的问题。所有新开的Issues都会自动收集到这里来。(目前貌似自动收集的功能有点问题，请点右上角Add Cards手动把Issue拖进来)
- 已完成：已经搞定了的项目。

工作的流程就是，
1. 当一个Issues讨论被敲定之后，别忙着Close，把它从讨论中拖到任务队列。
2. 当你把事情搞定之后，再把任务队列里相应的卡片拖到已完成那里。（也可以通过关闭Issues来达到同样的效果）
3. 你会发现标题那里的进度条推进了一格。给你一朵小红花。

## license
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />本汉化项目 采用 <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a>进行许可。


### if you have any question, please post it in issues
### Welcom to our [Current Status Board](https://github.com/MoHaDouBiTeam/gregtech6-chinese-translate/wiki/%E5%85%AC%E5%91%8A%E6%9D%BF-Current-Status)
