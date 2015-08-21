# coding=utf-8

import time
import os,sys
import subprocess

sys.setrecursionlimit(1000000)
def execTime(st):
    delt = time.time() - st
    print 'spend %.1fmin' %(delt/60)
st2 = time.time()
print 'start quick_sort...'
quick_sort = os.system(r'C:\Users\ieware\pyexercises\quick_sort.py')
print 'end quick_sort...',execTime(st2)
if quick_sort != 0:
    print 'quick_sort error'
    raise
st3 = time.time()
print 'start merge_sort...'
merge_sort = os.system(r'C:\Users\ieware\pyexercises\merge_sort.py')
print 'end merge_sort...',execTime(st3)

