
qa string
import string,random
import ast
import re
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

list2 = ['a','b','c','d','db','thanks']
str2 = 'welcome!'

1 ''.join()用法
print '1...'
print '-'.join(list2) # -为分隔符，把list转为str
2 字符转换成小写
print '2...'
print str2.lower() # upper()大写
3 字符串转化成float/int
print '3...'
int(),float()
print ast.literal_eval('532.13')
4 反序输出字符串
print '4...'
print str2[::-1]
5 随机生成数字大小写的字符串
print '5...'
print ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase+ string.digits) for x in range(7))
6 判断一个字符串是数字
print '6...'
def is_number(str2):  # 也可以用isdigit，但是对非整数无效
    try:
        float(str2)
        return True
    except ValueError:
        return False
字符串格式化 % 和.format % 一般传入变量或者元祖
print '7...'
print "test {kwarg}".format(kwarg=str2) # 也可以print "test2 %s" %{'kwarg':str2}
print 'test %s'%(str2,) # 可能会报TypeError异常
8 将字符串转化成字典
print '8...'
print ast.literal_eval("{'a' : 'b', 'c' : 'd'}")  # 字符串内需对于字典内容
9 获取一个字符的ASCII码
print ord('a'),chr(97)
print unichr(97),unichr(1234)
10 使用不同的分隔符切分字符串
print '10...'
print re.split('\W+', 'Words, words, words.')
print re.split('(\W+)', 'Words, words, words.')
print re.split('\W+', 'Words, words, words.', 1)
11 如何截掉空格或者tab
print '11...'
str3 = '\t a string example \t'
str3 = str3.strip()  # 空白在字符串左右两边
str3 = str3.rstrip()  # 空白字符在右边
str3 = str3.lstrip()  # 空白字符在左边
str3 = str3.strip('\t\n\r')  # 使用strip里作为截掉字符参数
12 如何截取一个字符串作为子串
print '12...'
print str2[:-2]  # 可以直接用切片方式
13 python用==比较字符串，is有时候会返回错误判断
print '13...'
a = 'pub'
b = ''.join(['p','u','b'])
print a == b  # ==是相等测试
print a is b  # is是身份测试相当于id(a) == id(b)
14 填充字符串
print '14...'
n = '3'
print n.zfill(5)
print '000007%d' %(int(n))
print '{0:03d}'.format(5)
print '{0:.3f}'.format(0.2347)
15 如何把字符串转化为datetime
print '15...'
pub = time.strftime("%a,%d %b %Y %H:%M:%S +0000",time.gmtime())
print pub
16 如何将byte array转为string
print '16...'
b"abcde"
b"abcde".decode('utf-8')
取索引
for index,x in enumerate(list2):print index,x
#global list2 #  在函数使用global变成全局变量

windows 文本默认格式ansi,在sublime会乱码
UTF-8是Unicode的实现方式之一
字符串可以编码成字节包, 字节包可以解码成字符串
在utf8的文件中，字符串为utf8编码，在gb2312的文件中，编码为gb2312
str是字节串, 经过unicode编码(encode)的字节串
utf-8是经过
decode() 其他编码转化成unicode编码
encode() unicode编码转为其他编码
b'\xe4\xb8\xad\xe6\x96\x87'
s = '中文' # '\xe4\xb8\xad\xe6\x96\x87'
s.encode('utf-8')
unicode(s) # return u'\u4e2d\u6587'
s.encode('utf-8') # '\xe4\xb8\xad\xe6\x96\x87'
s = '\u4e2d\u6587'
s.decode('unicode-escape')
16进制转换
'68656c6c6f'.decode("hex")
from subprocess import check_output
t = check_output('ipconfig')
t.decode('gbk')
