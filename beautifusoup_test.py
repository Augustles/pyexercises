# coding=utf-8

from bs4 import BeautifulSoup

with open(r'c:\users\ieware\index.html') as f:
    soup = BeautifulSoup(f) # ��beautifulsoup����
    #print soup.title,soup.title.text,soup.title.name
    #print soup.head,soup.body,soup.p,soup.a,soup.find_all('a')
    print soup.a.text
    print soup.find_all('title'),soup('title')
    #for link in soup.find_all('a'): # �ҵ�a��ǩ
        #print link.get('href') # ��ȡ����ҳ����������

    #print soup.get_text() # ��ȡ���е��ı���Ϣ
