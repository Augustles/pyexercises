# coding=utf-8

'''
Given s = "Hello World",
return 5.
'''

def lengthOfLastWord(s):
    return len(s.strip().split()[-1])

if __name__ == '__main__':
    s = "Hello World"
    print lengthOfLastWord(s)
