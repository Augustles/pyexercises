# coding=utf-8

'''
Given s = "the sky is blue",
return "blue is sky the".
'''

def reverseWords(s):
    return ' '.join(s.strip().split()[::-1])

if __name__ == '__main__':
    s = "the sky is blue"
    print reverseWords(s)
    print s.split(),' '.join(s.split()[::-1])
    
