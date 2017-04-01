# coding=utf-8

import asyncio
import threading

# python3.4
# python3.5 async def hi():
@asyncio.coroutine # 声明这是一个generator
def hi():
    # python3.5 await asyncio.sleep(1)
    yield from asyncio.sleep(1) # yield from 调用另外一个generator
    print('hi you are in %s' %threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hi(), hi()]
# 把generator放到loop中
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


