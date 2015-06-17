# coding=utf-8

'''
a = "11"
b = "1"
Return "100".
'''

def addBinary(a,b):
    return str(bin(int(a,2)+int(b,2))[2:])

if __name__ == '__main__':
    a = "11"
    b = "1"
    print addBinary(a,b)
