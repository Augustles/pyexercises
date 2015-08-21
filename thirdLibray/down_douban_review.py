# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import requests
import os,re
import time
import multiprocessing

t_sumary = []
t_pic = []
t_review = []
# headers可能导致403
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Cookie':'bid="KkJmbgQSS6U"; ll="118282"; _ga=GA1.2.1950220588.1437556212; ct=y; viewed="3434316"; __utma=30149280.1950220588.1437556212.1438845723.1438853846.11; __utmz=30149280.1438242497.8.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1439368832%2C%22http%3A%2F%2Fmovie.douban.com%2Fsubject%2F25953663%2Fdoulists%22%5D; bid="PUmaYqiOax8"; ll="118282"; _pk_ses.100001.8cb4=*; Hm_lvt_f5127c6793d40d199f68042b8a63e725=1439369662; Hm_lpvt_f5127c6793d40d199f68042b8a63e725=1439370508; _5t_trace_sid=41869e0c1e7f41b8993ffdba678fd0cb; _5t_trace_tms=1; dbcl2="65041622:VIWA/NF86AU"; ck="N76w"; push_noty_num=0; push_doumail_num=6; ap=1; push_noty_num=0; push_doumail_num=6; _pk_id.100001.8cb4=c1bceaa5c239e3f5.1437556262.22.1439458972.1439366798.; _pk_ses.100001.8cb4=*; ap=1',
    }

# 获取简介
def get_sumary(url):
    t1 = time.time()
    s = requests.Session()
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text)
    actors = []
    for a in soup.find_all('a', attrs = {'rel':'v:starring'}):
        actors.append(unicode(a.text)+' ')
    for v in soup.find_all(id='link-report'):
        global sub
        sub = unicode(soup.title.text)[:-5].strip()
        file_sumary = unicode(sub)+u' 简介'+u'.txt'
        print(u'...开始获取<<{0}>>简介...'.format(sub))
        with open(file_sumary,'a') as a:
            a.write(u'剧名: '+sub + u'\n' + u'主演: ')
            a.writelines(actors)
            y = unicode(v.span.text).strip()
            a.write('\n'+u'简介: '+''.join(y.split())+'\n')
    t2 = time.time()
    t3 = t2 - t1
    t_sumary.append(t3)
    print('get_sumary done')

# 获取照片
def get_pic(url):
    t1 = time.time()
    print('downloading <<{0}>> pictures...'.format(sub))
    r = requests.get(url,headers=headers)
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
    d = list(set(d)) # 去除重复的项
    for pic in d:
        file = pic[pic.rindex('/p')+1:]
        r = requests.get(pic)
        with open(file,'wb') as w:
            w.write(r.content)
    t2 = time.time()
    t3 = t2 - t1
    t_pic.append(t3)
    print('download jpg done')

# 全部照片
# l = 'http://movie.douban.com/subject/26367601/photos?type=S&start=40&sortby=vote&size=a&subtype=a'
# def all_pic(l2):
#     r = requests.get(l2)
#     s = bs(r.text)
#     for n in s.find_all('span',attrs={'class':'count'}):
#         m = re.findall(r'\d+',n.text)
#         length = round(int(m[0])/40.0+1)
#         print length
#     e = int(40 * length)
#     subjects = []
#     f = range(0,e,40)
#     for n in f:
#         num = 'start='+ str(n)
#         url = re.sub(r'start\=\d+', num, l2)
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text)
#         n = 0
#         for joke in soup.find_all('div', attrs={'class':'cover'}):
#             n = n + 1
#             thumb =  joke.a.img['src']
#             photo = thumb.replace('/thumb','/photo')
#             # subjects.append(photo)
#             file = photo[photo.rindex('/p')+1:]
#             r = requests.get(photo)
#             print r.status_code
#             with open(file,'wb') as w:
#                 w.write(r.content)
            
#     # for photo in subjects:
#     #     file = photo[photo.rindex('/p')+1:]
#     #     r = requests.get(photo)
#     #     print r.status_code
#     #     with open(file,'wb') as w:
#     #         w.write(r.content)


# 获取影评
def get_review(url):
    t1 = time.time()
    print(u'...获取<<{0}>>热点影评...'.format(sub))
    r = requests.get(url,headers=headers)
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
        x = re.sub('[?|<>,/\:*"]',' ',x)
        try:
            with open(x.decode('utf8'),'w') as w:
                w.write(x[:-4] + '\n')
                w.write(y)
        except Exception,e:
            with open('down.log','a') as a:
                a.write('\n'+time.strftime('%Y-%m-%d %H:%M:%S')+' <=> '+e.message)
    t2 = time.time()
    t3 = t2 - t1
    t_review.append(t3)
    print('get_review done')

# 获取subjects
def get_subjects(doulists):
    print('...start project...')
    start = time.time()
    global subjects
    subjects = {}
    f = range(0,300,25)
    for n in f:
        num = 'start='+ str(n)
        url = re.sub(r'start\=\d+', num, doulists)
        r = requests.get(url, headers=headers)
        print(r.status_code,r.url)
        soup = BeautifulSoup(r.text)
        for joke in soup.find_all('div', attrs={'class':'title'}):
            sub = joke.text.strip()
            subjects[sub] = joke.a['href']
    print(u'...本豆列有{0}项...'.format(len(subjects)))
    # 多进程测试
    return subjects
    pre_path = os.getcwd()
    for item in zip(range(1,len(subjects)+1),subjects.keys(),subjects.values()):
        global sub_id
        sub_id = item[0]
        x = item[1]
        y = item[2]
        if not os.path.exists(x):
            print(u'开始第 {0} 个subject < {1} >'.format(sub_id,y))
            # 文件名中不允许出现字符/\:*?
            remove = ['/','\\',':','*','?','\"','<','>','|']
            x = re.sub('[?|<>,/\:*"]','',x)
            try:
                os.mkdir(x)
                os.chdir(x)
                get_sumary(y)
                #get_review(y)
                #get_pic(y)
            except Exception,e:
                with open('down.log','a') as a:
                    a.write('\n'+time.strftime('%Y-%m-%d %H:%M:%S')+' <=> '+e.message)
        else:
            print(u'忽略第 {0} 个subject < {1} > 已存在!!!'.format(sub_id,y))
            # with open('down.log','a') as a:
            #     a.write('\n'+time.strftime('%Y-%m-%d %H:%M:%S')+' <=> '+u'忽略第 {0} 个subject < {1} > 已存在!!!'.format(sub_id,y))
            # continue  


        os.chdir(pre_path)
        
    # 判断doulists是否完成
    if len([dir for dir in os.listdir(pre_path)]) < len(subjects) + 1:
        get_subjects(doulists)
    else:
        end = time.time()
        spend = (end - start) / 60
        print(u'...下载已经完成, 总共花费 <{0:.2f}> mins...'.format(spend))
        print(u'sumary用时{0:.2f}'.format(sum(t_sumary)/60,))
        print(u'review用时{0:.2f}'.format(sum(t_review)/60,))
        print(u'pic用时{0:.2f}'.format(sum(t_pic)/60,))

doulists = 'http://www.douban.com/doulist/38849533/?start=50&sort=seq&sub_type='
# doulists1 = 'http://www.douban.com/doulist/3151243/?start=25&sort=time&sub_type='
url = u'http://movie.douban.com/subject/10491666/'
# get_sumary(url)
# get_pic(url)
# get_review(url)

# 记录异常
# try:
#     get_subjects(doulists)
# except:
#     f = open('down.log','a')
#     import traceback
#     f.write('\nError: <=> \n')
#     f.write(time.strftime('%Y-%m-%d %H:%M:%S')+' <=> ')
#     traceback.print_exc(file=f)
#     f.flush()
#     f.close()
# finally:
#     with open('down.log','a') as a:
#         a.write('\n'+time.strftime('%Y-%m-%d %H:%M:%S') + u' <=> 完成 {0} 下载'.format(doulists))


get_subjects(doulists)
links = subjects.values()
def test_process(link):
    print(time.strftime('%Y-%m-%d %H:%M:%S') + 'test_process start...')
    r = requests.get(link,headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.text)
    print(soup.title.text)


# 多进程实践
if __name__ == '__main__':
    try:
        # 作用于线程
        # pool = multiprocessing.Pool(processes=10)
        # # links为一个序列
        # result = pool.map_async(get_sumary, links).get(240)
        
        # 作用于进程,需import dummy否则提示没有dummy
        from multiprocessing import dummy
        pool = dummy.Pool(processes=10)
        result = pool.map_async(get_sumary, links).get(240)
    except Exception,e:
        print e
