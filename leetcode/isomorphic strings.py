# coding=utf-8

'''
判断两个字符串能否相互映射
'''

def isomorphic(s,t):
    if s is None and t is None:
        return True
    if s == t:
        return True
    mp = {}
    for i in range(len(s)):
        if mp[s[i]] != t[i]:
            return False
        else:
            if t[i] in t[0:i]:
                return False
            mp[s[i]] = t[i]
        return True
