# coding=utf-8

from multiprocessing import Process, current_process

# 导入process，Python的线程在多核情况下的性能是比较低的

def test(*args,**kw):
    p = current_process()
    print p.name
    print args,kw

if __name__ == '__main__':
    p = Process(target=test,args=(1,3,5),kwargs={'a':3},name='TEST')
    p.start() # 开创子进程，参数args，kwargs会传递给test函数
    p.join() # join()等待并获取子进程退出状态
