# coding=utf-8

'''
多个字符串的最长公共前缀
'''

def longestComonPrefix(strs):
    if not strs:
        return ''
    for x,value in enumerate(zip(*strs)):
        if len(set(value)) > 1:
            return strs[0][:x]
        else:
            return min(strs)
