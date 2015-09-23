# encoding=utf-8


def coroutine(func):  # 防止忘记调用.next()函数
    def start(*args, **kargs):
        cr = func(*args, **kargs)
        cr.next()
        return cr
    return start


import time


def follow(thefile, target):
    thefile.seek(0)      # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)    # Sleep briefly
            continue
        target.send(line)


@coroutine
def broadcast(targets):  # targets是coroutine集合, list
    while True:
        item = (yield)
        # print item
        for target in targets:
            # print target
            target.send(item)


@coroutine  # 从上一个coroutine接收
def grep(pattern, target):  # target是coroutine
    print 'looking for {0}'.format(pattern)
    while True:
        line = (yield)  # 挂起, 等待接收line数据
        if pattern in line:  # 数据符合要求则
            target.send(line)  # 发送到下一个coroutine处理


@coroutine
def printer():
    while True:
        line = (yield)
        print line,


if __name__ == '__main__':
    f = open("cobroadcast2.py")
    p = printer()
    l = ['python', 'ply', 'swig']
    # for x in l:
    #     follow(f, grep(x, p))
    follow(f,
           broadcast([grep('python', p),
                      grep('ply', p),
                      grep('swig', p)])
           )
