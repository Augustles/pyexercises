# coding=utf-8

# 保存写入时候出现UnicodeEncodeError:ascii
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# requests-future
import requests
import grequests  # requests并发库 pip install grequests
urls = ["http://www.baidu.com/"] * 100
from bs4 import BeautifulSoup as bs
import re

# reqs = [grequests.get(url) for url in urls]
# response = grequests.map(reqs)
# for x in response:
#     print('GET: {0} {1}'.format(x.status_code, x.url))

# pool = grequests.Pool()
# def s(url):
#     r = requests.get(url)
#     print("GET: {0} {1}".format(r.status_code, r.url))
# for x in urls:
#     pool.spawn(s, x)
# pool.join()

# for x in urls:
#     r = requests.get(x)
#     print('GET: {0} {1}'.format(r.status_code,r.url))

# requests 中文乱码
# print(u'\u6c34\u8349\u739b\u7459')
# import requests # 导入requests，需要pip安装
# from bs4 import BeautifulSoup # 安装pip install beautifulsoup4
# r = requests.get('https://github.com/timeline.json')  # 发送一个get请求，相应有post
# print r.text,r.content,r.encoding,r.status_code() # 响应内容,二进制响应内容,编码,响应状态码
# print r.json(),r.raw() # json响应内容，原始响应内容
# print r.headers
# print r.text
# 进行编码处理, 防止乱码

# coding=utf-8

# import requests
# import urllib
# import chardet # 检测字符编码
# from bs4 import BeautifulSoup

# # 防止出现UnicodeEncodeError
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# url = 'http://www.liaoxuefeng.com/'
# testData = urllib.urlopen(url).read() # 读取内容
# r = requests.get(url) # 中文乱码???
# #print chardet.detect(testData) # 检测字符
# soup = BeautifulSoup(testData)

# title = soup.title.text # 有时提示没有text属性,用try:
# keywords = soup.select('meta[name="keywords"]')
# description = soup.select('meta[name="description"]')
# print url,title,keywords,description,soup.p

# import chardet
# r.encoding = chardet.detect(r.content)['encoding'] # requests设置encoding
# r.content.decode(chardet.detect(r.content)['encoding']) # 字符串decode
# soup = bs(r.text)
# print soup.title.text

# 测试代理ip是否可用
# proxies = {
#     'http': '61.130.97.212:8099',
# }


# r = requests.get("http://ip.chinaz.com/", proxies=proxies, timeout=5)
# print r.request.headers
# print bs(r.content).find('span', attrs={'class': 'info3'}).strong.get_text()

# m = requests.get('http://mnwg.net')
# s = BeautifulSoup(m.text)
# title = s.title.contents # string
# keywords = s.select('meta[name="keywords"]')
# description = s.select('meta[name="description"]')
# print(title,description,keywords)

# for meta in s.find_all('meta'):
#     print(meta.get('name'))

# 写入test.html
# with open('test.html', 'a+') as f:
#     for line in m.text:
#         f.write(line)


# headers = {
#     'Cookie':'Cookie: _za=a9a7a089-55d0-4e7b-8239-82c639c8102a; __utma=51854390.2118762785.1438156422.1439783263.1439789466.7; __utmz=51854390.1439789466.7.7.utmcsr=s.bt.gg|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|3=entry_date=20150729=1; q_c1=ec104df951094b318fc5284eba306fe1|1440994756000|1438156321000; cap_id="YzU2ZmUxMGNhN2IyNDMzN2FjMzFmNGFhNGNjZmRmMzE=|1440994756|3c5b0b31ef22c7cf92b6950c9c6c237f673265db"; _xsrf=d078156ca3f4d6287a7979324efb98fe&password=zhaoying&remember_me=true&email=1927064778%40qq.com',
#     'Origin':'http://www.zhihu.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
#     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#     'Referer':'http://www.zhihu.com/',
#     'Accept-Language':'zh-CN,zh;q=0.8',
#     'Host':'www.zhihu.com',
#     'Connection':'keep-alive',
#     'Content-Length:':'99',
#     'Accept':'*/*',
#     'X-Requested-With':'XMLHttpRequest',
# }
# ss = requests.session()
# ss.headers.update(headers)

# ss.post('http://www.zhihu.com/#login', data={
#     '_xsrf': bs(requests.get('http://www.zhihu.com/').content).find(type='hidden')['value'],
#     'email': '1927064778@qq.com',
#     'password': '',
#     'rememberme': 'true'})
# r = ss.get('http://www.zhihu.com',headers=headers)
# print r.content

# ss = requests.session()
# headers = {
#     'Host': 'www.8dwww.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:39.0) Gecko/20100101 Firefox/39.0',
#     'Referer': 'http://www.8dwww.com/',
#     'Cookie': 'ASPSESSIONIDASRCTAQS=EPPDLOKBFIHLMPANFKDGNHMB; IESESSION=alive; bdshare_firstime=1440999947377; Hm_lvt_f5127c6793d40d199f68042b8a63e725=1440999948; Hm_lpvt_f5127c6793d40d199f68042b8a63e725=1441000038; pgv_pvi=756273152; pgv_si=s9144142848; _5t_trace_sid=92df0838b03c9e2a92a2e0efe5405b57; _5t_trace_tms=1; Hm_lvt_19a5cb6dc0bc4f92dea1d7f09bea43aa=1440999985; Hm_lpvt_19a5cb6dc0bc4f92dea1d7f09bea43aa=1441000037',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# }

# ss.post('http://www.8dwww.com/user/userlogin.asp', data={
#     'username': 'cxk517',
#     'password': '',
#     'submit': 'Login',
# })
# r = ss.get('http://www.8dwww.com/user/logininfo.asp')
# print r.status_code
# import chardet
# r.encoding = chardet.detect(r.content).get('encoding')
# print r.text


# ss = requests.session()
# headers = {
#     'Host': '192.168.0.120:8000',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:39.0) Gecko/20100101 Firefox/39.0',
#     'Referer': 'http://192.168.0.120:8000/accounts/login/',
# 'Cookie':'ASPSESSIONIDASRCTAQS=EPPDLOKBFIHLMPANFKDGNHMB; IESESSION=alive; bdshare_firstime=1440999947377; Hm_lvt_f5127c6793d40d199f68042b8a63e725=1440999948; Hm_lpvt_f5127c6793d40d199f68042b8a63e725=1441000038; pgv_pvi=756273152; pgv_si=s9144142848; _5t_trace_sid=92df0838b03c9e2a92a2e0efe5405b57; _5t_trace_tms=1; Hm_lvt_19a5cb6dc0bc4f92dea1d7f09bea43aa=1440999985; Hm_lpvt_19a5cb6dc0bc4f92dea1d7f09bea43aa=1441000037',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# }

# csrf = ss.get('http://192.168.0.120:8000/accounts/login/')
# soup = bs(csrf.text)
# i = soup.find('input').get('value')
# print i

# ss.post('http://192.168.0.120:8000/accounts/login/', data={
#     'username': '1927064778@qq.com',
#     'password': 'cxk517',
#     'csrfmiddlewaretoken': i,
# })
# r = ss.get('http://192.168.0.120:8000/my',)
# print r.status_code
# print r.text
