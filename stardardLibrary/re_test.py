# coding=utf-8

import re # 正则表达式
# re.findall(),sub(),search(),match,

# 正则表达式的元字符.^$*?{}[]|()
# .表示任意字符
# []用来匹配一个指定的字符类别
# ^放在字符串开头,取非
# $放在字符串结尾,须以作为结束
# +匹配到一个及以上
# *对前一个字符重复0到无穷次
# ?对前一个重复0到1次
# {m,n}对前一个重复在m到n次之间
# {m}对前一个字符重复m次

# \d 匹配任意十进制数,相当于类[0-9]
# \D 匹配任意非数字字符,相当于类[^0-9]
# \s 匹配任意空白字符,相当于类[ fv]
# \S 匹配任意非空字符,相当于类[^ fv]
# \w 匹配任意数字字母字符,相当于[a-zA-Z0-9_]
# \W 匹配任意非数字字母字符,相当于类[^a-zA-Z0-9_]

text = "JGood is a handsome boy, he is cool, clever, and so on..."
text1 = text[:]
print re.findall(r'\w+', text) # 返回一个列表
print re.sub(r'\s+','_', text) # 替换匹配到的字符
m = re.search(r'o\w+', text) # 返回匹配到第一个值
print m.group(),m.start(),m.end()
m1 = re.split(r'\s+', text) # 按照条件分割字符串
print m1

print '-'.join(m1)
print text1.find('handsome') # 返回h的索引
print text1.replace('boy','girl') # replace方法替换
print text1.split(),type(text1)

# 常用正则表达式,匹配中文 [\u4e00-\u9fa5]
# 匹配双字节字符(包括汉字在内)：[^\x00-\xff]
# 匹配空白行的正则表达式：\n\s*\r
# 匹配HTML标记的正则表达式：<(\S*?)[^>]*>.*?</\1>|<.*? />
# 匹配首尾空白字符的正则表达式：^\s*|\s*$
# 匹配Email地址的正则表达式：\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*
# 匹配网址URL的正则表达式：[a-zA-z]+://[^\s]*
# 匹配国内电话号码：\d{3}-\d{8}|\d{4}-\d{7}
# 匹配腾讯QQ号：[1-9][0-9]{4,}
# 匹配身份证：\d{15}|\d{18}
# 匹配ip地址：\d+\.\d+\.\d+\.\d+
