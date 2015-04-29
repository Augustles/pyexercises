# coding=utf-8

from threading import * # 导入Threading
import time

def thread_test(s):
    print 'ident:',currentThread().ident #
    time.sleep(2) # 程序休眠1秒
    print 'count:', activeCount() # 当前进程中线程的个数
    print s

if __name__ == '__main__':
   for x in xrange(1,10):
        Thread(target = thread_test, args = ("Hello",)).start()
        for item in enumerate(): # 返回当前运行中的Thread对象列表
            print item

    #t.setDaemon(True)
    #t.start()

