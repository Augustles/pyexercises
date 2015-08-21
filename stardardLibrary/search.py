# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os

# window搜索中文不可用
def search(word,path='.'):
    d = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt') or file.startswith('search.py'):
                pass
            else:
                d.append(os.path.abspath(root+os.sep+file))
    for file in d:
        if word in file:
            print(file)
            # break
        else:
            with open(file) as f:
                for line in f:
                    if word in line:
                        if os.name == 'nt':
                            print(file.replace('\\','/'),line)
                        else:
                            print(file,line)
                        # break
word = input('which to research : ')
search(word)
if os.name == 'nt':
    import msvcrt
    msvcrt.getch()
