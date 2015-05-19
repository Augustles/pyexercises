#!/usr/bin/env python
# encoding: utf-8

# 去除文件中的空行


def rmblankline(f1, f2):
    infp = open(f1, 'r')
    outfp = open(f2, 'w')
    lines = infp.readlines()
    for line in lines:
        if line.split():
            outfp.writelines()
    infp.close()
    outfp.close()

# def rmchompline(f1,f2):
#     with open(f1) as f:
#         x = f.readlines()
#         x.splitlines()
#         f2.writelines(x)
if __name__ == '__main__':
    rmblankline(f1, f2)  # f1是需要去除空行文件
