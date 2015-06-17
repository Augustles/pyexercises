# coding=utf-8

# 多进程实践
import os

##print 'process (%s) start...' % os.getpid()  # 获取父进程pid
##pid = os.fork()

from multiprocessing import Process

def run_proc(name):
    return 'run child process %s' %os.getpid()

if __name__ == '__main__':
    print 'parent process %s'%os.getpid()
    p = Process(target=run_proc,args=('test',))
    print 'process will start'
    p.start()
    print p
    p.join()
    print 'process end.'
