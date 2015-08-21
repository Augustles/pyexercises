# coding=utf-8

# pip install passlib
# http://pythonhosted.org/passlib/genindex.html
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt, sha1_crypt
password = '123456'
sha1 = sha1_crypt.encrypt(password)
md5 = md5_crypt.encrypt(password) # /etc/shadow
sha256 = sha256_crypt.encrypt(password)
sha512 = sha512_crypt.encrypt(password)
print(md5,sha256,sha512,sha1)
md5_crypt.verify(password, md5) # 验证password和hash值
