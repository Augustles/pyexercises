# coding=utf-8

import os


def list_file(path):  # 列出所有文件(包含子文件)
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            all_files.append(os.path.abspath(root + os.sep + file))
    return all_files


def list_file_content(file):  # 列出单个文件内容
    file_content = []
    try:
        with open(file) as f:
            file_content.append(f.readlines())
    except Exception, e:
        print e
    return file_content


if __name__ == '__main__':
    print os.getcwd()
    files = list_file('')
    map(list_file_content, files)
