# coding=utf-8

'''
从标题就可以知道题意了，是求一个字符串中最长的不含重复字符的子串。
'''

def longestSubstring(s):
    res = 0
    left = 0
    d = {}

    for i, ch in enumerate(s):
        if ch in d and d[ch] >= left:
            left = d[ch] + 1
        d[ch] = i
        res = max(res, i - left + 1)
    return res
