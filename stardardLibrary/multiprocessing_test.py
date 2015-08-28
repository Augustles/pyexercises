# coding=utf-8

# 多进程实践
import os

# print 'process (%s) start...' % os.getpid()  # 获取父进程pid
# pid = os.fork() fork的系统调用只存在linux/unix中

import multiprocessing
multiprocessing.freeze_support() # windows下崩溃
# def run_proc(name):
#     return 'run child process %s' %os.getpid()

# if __name__ == '__main__':
#     print 'parent process %s'%os.getpid()
#     p = multiprocessing.Process(target=run_proc,args=('test',))
#     print 'process will start'
#     p.start()
#     print p
#     p.join()
#     print 'process end.'


def printf(x):
    return x

l = range(3, 9)
l.insert(0, 'hello')
l.append('august')

if __name__ == '__main__':
    # processes需合理设置
    # pool = multiprocessing.Pool(processes=2)
    # 相当于for循环执行l里的元素
    # printf为执行的函数, l为要执行的序列元素
    # result = pool.map_async(printf,l).get(120)

    pool = multiprocessing.Pool(4)
    result = []
    for x in l:
        result.append(pool.apply_async(printf,args=(x,)))
    pool.close()
    pool.join()
    for y in result:
        print y.get()

    # jobs = []
    
    # from multiprocessing.dummy import Process,Pool
    # for x in l:
    #     p = Process(target=printf,args=(x,))
    #     jobs.append(p)
    #     p.start()

    
