# coding=utf-8

'''
比较两个版本号version1和version2。
'''

def compareVersion(ver1,ver2):
    v1 = [int(s) for s in ver1.split('.')]
    v2 = [int(s) for s in ver2.split('.')]
    v1 += [0] * (max(len(v1), len(v2)) - len(v1))
    v2 += [0] * (max(len(v1), len(v2)) - len(v2))
    return cmp(v1,v2)

if __name__ == '__main__':
    version1 = '2.3.5'
    version2 = '1.9.98'
    print compareVersion(version1,version2)
