# coding=utf-8

from bs4 import BeautifulSoup as bs
import requests

# with open(r'c:\users\ieware\index.html') as f:
# soup = bs(f)  # 用beautifulsoup解析
# print soup.title,soup.title.text,soup.title.name
# print soup.head,soup.body,soup.p,soup.a,soup.find_all('a')
# print soup.a.text
# print soup.find_all('title'), soup('title')
# for link in soup.find_all('a'):  # 找到a标签
#     print link['href']
# print link.get('href') # 获取整个页面所有链接
# print soup.get_text() # 获取所有的文本信息


# soup.find('div', attrs={'class': 'title'})
# soup.find('div', attrs={'class': None, 'id': True})  # limit=3返回限定3数量

# headers部分一般没有cookies, 由服务端返回
headers = {'Cookie': 'CNZZDATA4793016=cnzz_eid%3D207825403-1441784021-%26ntime%3D1441866136',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'}

r = requests.get('http://www.kuaidaili.com/free/', headers=headers)
soup = bs(r.text)

# all
all = soup.find('table', attrs={
    'class': 'table table-bordered table-striped'}).find_all('tr')[1:]

# one
for x in all:
    info = x.find_all('td')
    ip = info[0].get_text(strip='\r\n')
    port = info[1].get_text(strip='\r\n')
    http = info[3].get_text(strip='\r\n')
    print ip, port, http
