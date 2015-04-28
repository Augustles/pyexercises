# coding=utf-8

from bs4 import BeautifulSoup

with open(r'c:\users\ieware\index.html') as f:
    soup = BeautifulSoup(f) # 用beautifulsoup解析
    #print soup.title,soup.title.text,soup.title.name
    #print soup.head,soup.body,soup.p,soup.a,soup.find_all('a')
    print soup.a.text
    print soup.find_all('title'),soup('title')
    #for link in soup.find_all('a'): # 找到a标签
        #print link.get('href') # 获取整个页面所有链接

    #print soup.get_text() # 获取所有的文本信息
