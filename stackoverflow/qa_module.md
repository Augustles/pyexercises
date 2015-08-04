
module模块

1. __init__.py是做什么用的
这是包的一部分,__init__让python把目录当成包
2.如何使用绝对路径import一个模块
import imp
foo = imp.load_source('module.name','qa_module.py')
3.获取python模块文件的路径
import os
print os.__file__
4.谁可以解释一下all?
print os.__all__
该模块的公有对象列表
5.如何重新加载一个python模块
使用reload()内置函数
6.在python中,如何表示Enum(枚举)
from enum import Enum
animal = Enum('animal','ant bee cat dog')
7. if __name__ == '__main__':做了什么?
理解为判断是否直接运行
8.通过使用相对路径引用一个模块
import os, sys, inspect
realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

use this if you want to include modules from a subfolder
cmd_subfolder=os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

Info:
cmd_folder = os.path.dirname(os.path.abspath(__file__)) # DO NOT USE__file__ !!!
__file__ fails if script is called in different ways on Windows
__file__ fails if someone does os.chdir() before
sys.argv[0] also fails because it doesn't not always contains the path
9. python中如何进行间接引用
