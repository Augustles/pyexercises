# python小结
###string
	s = 'hello august'
1. s.capitalize() 首字母大写
2. s.find('aug') 返回a切片的索引
3. s.isspace() s只包含空格
4. s.partition()
5. s.rstrip() 去除右边空白
6. s.translate()
7. s.center()
8. s.format()
9. s.istitle() bool,
10. s.replace('august','ttoo') 替换为ttoo
11. s.split()
12. s.upper() s字符串转成大写
13. s.count('l') 返回l出现次数
14. s.index('o') 返回o切片索引
15. s.isupper() bool,s是否全部大写
16. s.rfind()
17. s.splitlines()
18. s.zfill(16) 填充'0'至16位
19. s.decode('utf8') 解码成unicode,utf8
20. s.isalnum() bool,是否仅包含0~9,a~z,A~Z
21. s.join()
22. s.rindex()
23. s.startswith('he') bool,是否以'he'开始
24. s.encode('utf8') 编码, 编码为utf8格式
25. s.isalpha() bool,是否仅包含a~z,A~Z
26. s.ljust()
27. s.rjust()
28. s.strip() 去除左右边空白
29. s.endswith('oo') bool,是否以'oo'结束
30. s.isdigit() bool,是否仅包含0~9
31. s.lower() 转为小写
32. s.rpartition()
33. s.swapcase() 大小写相互转换
34. s.expandtabs()
35. s.islower() bool,是否全部为小写
36. s.lstrip() 去除左边空白
37. s.rsplit()
38. s.title() 单词首字母大写

###list(array)
	l = [True,'hello',1,87]
1. l.append('tty') 添加tty到l末尾
2. l.extend(['x','y']) 添加x和y末尾
3. l.insert(1,23) 在l[1]前插入23
4. l.count(1) 返回1出现次数
5. l.index(87) 返回87出现切片位置
6. l.pop() 去除末尾最后一个值
7. l.reverse() 反转l相当于l[::-1]
8. l[0] 取第一个元素值
9. del l[0] 删除第一个元素值
10. s[i:j] = 33 用33替换[i:j]
11. del s[i:j] 相当于s[i:j] = []

###dict(hash)
	d = {'x':3,'y':4}
1. d.clear() 清空字典d
2. d.get('x') 取'x'value
3. d.iteritems() 可迭代对象的(key,value)
4. d.keys() 可迭代对象keys值
5. d.setdefault()
6. d.viewitems() dict_items对象,key,value
7. d.copy() 赋值词典d
8. d.has_key('x') bool,是否存在key'x'
9. d.iterkeys() dictionary-itemiterator对象,keys迭代器
10. d.pop('x') 删除x及其value
11. d.update(d1) 根据d1更新数据
12. d.viewkeys() dict_items对象,keys
13. d.fromkeys('z','t') 创建字典d,key:'z','t',value:none
14. d.items() 返回[('y', 4), ('x', 3)]
15. d.itervalues() dictionary-itemiterator对象,values迭代器
16. d.popitem() 清空字典d,d为空则报错KeyError
17. d.values() 返回list
18. d.viewvalues() dict_items对象,values的视图
19. 'x' [not] in d 'x'是否在词典中(key)
20. 3 [not] in d.values() 3是否在value中
21. d['x'] 取词典d'x'的值
22. d['z'] = 33 设置key:z,value:33
23. del d['z'] 删除zkey和value