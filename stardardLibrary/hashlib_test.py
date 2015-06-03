# coding=utf-8

import hashlib # 摘要算法,又称哈希算法,散列算法,如md5,sha1

password = '123456'
salt = 'august'
password += salt
md5 = hashlib.md5()
md5.update(password.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1() # sha224,sha256,sha384,sha512
sha1.update(password.encode('utf-8'))
print(sha1.hexdigest())

print(hashlib.new('md5',password).hexdigest()) # 对单条数据加密
print(hashlib.new('sha512',password).hexdigest()) # sha512加密
