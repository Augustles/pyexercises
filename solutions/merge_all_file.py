# coding=utf-8

import os
import itertools
from list_files import list_file, list_file_content
# 合并文件夹的内容


def merge_all_file(dir):
    all_files = list_file(dir)
    contents = map(list_file_content, all_files)
    contents = list(itertools.chain(*contents))
    return contents
    # for content in contents:
    #     with open('demo.txt', 'a') as f:
    #         f.writelines(content)

if __name__ == '__main__':
    merge_all_file(os.getcwd())
