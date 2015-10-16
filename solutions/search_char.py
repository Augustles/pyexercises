# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os

# window搜索中文不可用?? 主要是编码解码问题


def search(word, path='.'):
    d = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt') or file.startswith('search.py'):
                pass
            else:
                d.append(os.path.abspath(root + os.sep + file))
    for file in d:
        if word in file:
            print(file.decode('gb2312').encode('gb2312'))
            # break
        else:
            with open(file) as f:
                for line in f:
                    if word in line:
                        if os.name == 'nt':
                            # import chardet # 用chardet判断什么编码,再进行decode和encode(一般为输出cmd出错)
                            # print chardet.detect(file.replace('\\', '/'))
                            print file.replace('\\', '/').decode('gb2312').encode('gb2312', 'ignore')
                            print line.decode('utf8').encode('gb2312', 'ignore')
                        else:
                            print(file, line)
                        # break
if os.name == 'nt':
    word = str(raw_input('which to research : '))
    word = word.decode('gb2312').encode('utf8')
else:
    word = input('which to research : ')

if __name__ == '__main__':
    search(word)
