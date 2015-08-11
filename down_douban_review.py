# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import requests


def get_sumary(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    actors = []
    for a in soup.find_all('a', attrs = {'rel':'v:starring'}):
        actors.append(unicode(a.text)+' ')
    for v in soup.find_all(id='link-report'):
        with open('sumary.txt','a') as a:
            global sub 
            sub = unicode(soup.title.text)[:-5].strip()
            print(u'开始获取<<{0}>>简介...'.format(sub))
            a.write(sub + '\n')
            for actor in actors:print(actor)
            a.writelines(actors)
            y = unicode(v.span.text).strip()
            print(''.join(y.split()))
            a.write('\n'+''.join(y.split())+'\n')
    print('get_sumary done')

def get_pic(url):
    print('downloading <<{0}>> pictures...'.format(sub))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    d = []
    for pic in soup.find_all('a'):
        if 'all_photos' in str(pic):
            r1 = requests.get(pic['href'])
            soup1 = BeautifulSoup(r1.text)
            for item in soup1.find_all('a'):
                if 'photos/photo' in str(item) and 'albumicon' in str(item):
                    if 'albumicon' in str(item.img['src']):
                        if str(item.img['src']) not in d:
                            d.append(str(item.img['src']).replace('albumicon','photo'))
    for pic in d:
        file = pic[pic.rindex('/p')+1:]
        r = requests.get(pic)
        print(file)
        with open(file,'wb') as w:
            w.write(r.content)
    print('download jpg done')



def get_review(url):
    print(u'获取<<{0}>>热点影评...'.format(sub))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    files = {}
    reviews = []
    for hot in soup.find_all('a', attrs = {'onclick':"moreurl(this, {from: 'review-hottest'})"}):
        if 'review' in str(hot):
            if hot['href'] not in reviews:
                reviews.append(hot['href'])
    for review in reviews:
        r1 = requests.get(review)
        soup1 = BeautifulSoup(r1.text)
        for title in soup1.find_all('meta', attrs={'name':'description'}):
            for body in soup1.find_all('div', attrs={'property':'v:description'}):
                file = str(title['content']) + '.txt'
                files[file] = unicode(body.text)
    for x,y in files.items():
        with open(x.decode('utf8'),'w') as w:
            print(x)
            w.write(x[:-4] + '\n')
            print(y)
            w.write(y)
    print('get_review done')


def get_subjects(doulists):
    global names, links
    subjects = {}
    f = range(0,300,25)
    import re,os
    for n in f:
        num = 'start='+ str(n)
        url = re.sub(r'start\=\d+', num, doulists)
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        for joke in soup.find_all('div', attrs={'class':'title'}):
            sub = joke.text.strip()
            subjects[sub] = joke.a['href']
    
    print(u'豆列有{0}项...'.format(len(subjects)))
    pre_path = os.getcwd()
    for x,y in subjects.items():
        if not os.path.exists(sub):
            os.mkdir(x)
        os.chdir(x)
        get_sumary(y)
        get_pic(y)
        get_review(y)
        os.chdir(pre_path)

doulists = 'http://www.douban.com/doulist/38849533/?start=50&sort=seq&sub_type='

url = u'http://movie.douban.com/subject/10491666/'
sub = '10491666'
# get_sumary(url)
# get_pic(url)
# get_review(url)
get_subjects(doulists)
