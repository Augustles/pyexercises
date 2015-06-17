# coding=utf-8

'''
回文palindrome
'''

def isPalindrome(s):
    s = filter(str.isalnum, str(s)).lower()
    return s = s[::-1]
