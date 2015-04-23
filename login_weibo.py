# coding = utf-8
# import �����Ҫע�����ֻ��һ��rsa���ģ������Ҫinstall�ģ������Ķ�������
import re , urllib.parse , urllib.request , http.cookiejar , base64 , binascii , rsa

# ����4�д���˵�򵥵�������������������get��post���󶼴����Ѿ���ȡ��cookie����Ϊ�Դ�Щ����վ�ĵ�½��֤ȫ��cookie
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support , urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

# ��װһ������get�ĺ���������΢�����get���������ݱ��붼��-8�����԰�utf-8д��������ˣ���ʵ��Ŀ�н����������ʵ�ʱ���������
def getData(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    text = response.read().decode('utf-8')
    return text

# ��װһ������post�ĺ�������֤������û�������post�ģ��������postData�ڱ�demo��ר��������֤�û���������
def postData(url , data):
  ��# headers��Ҫ�����Լ���ģ��
    headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'}
���� # �����urlencode���ڰ�һ�����������'&'�������ַ����������ž��Ǳ����utf-8
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url , data , headers)
    response = urllib.request.urlopen(request)
    text = response.read().decode('gbk')
    return text


def login_weibo(nick , pwd):
    #==========================��ȡservertime , pcid , pubkey , rsakv===========================
����# Ԥ��½���󣬻�ȡ�����ɲ���
    prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.15)&_=1400822309846' % nick
    preLogin = getData(prelogin_url)
����# �����ȡ���ĸ�ֵ���ǽ�����Ҫʹ�õ�
    servertime = re.findall('"servertime":(.*?),' , preLogin)[0]
    pubkey = re.findall('"pubkey":"(.*?)",' , preLogin)[0]
    rsakv = re.findall('"rsakv":"(.*?)",' , preLogin)[0]
    nonce = re.findall('"nonce":"(.*?)",' , preLogin)[0]
    #===============���û������������================
����# �ã����Ѿ�������½����΢�����ѵ�һ�����ˣ�����ⲿ��û�д������ָ��һ�£��Ǿ�����̫���ˣ���Ҳ�����˵ʲô���������Ǹ��ּ��ܣ�����γ��˼��ܺ��su��sp
    su = base64.b64encode(bytes(urllib.request.quote(nick) , encoding = 'utf-8'))
    rsaPublickey = int(pubkey , 16)
    key = rsa.PublicKey(rsaPublickey , 65537)
����# ��΢˵һ�µ������������ѵ��������У���Щ�����ﲢû�ж�ƴ���������ַ�������bytes������python3���·��������ǡ�rsa.encrypt��Ҫһ���ֽڲ�������һ���֮ǰ��һ������ʵ�����base64.b64encodeҲһ��
    message = bytes(str(servertime) + '\t' + str(nonce) + '\n' + str(pwd) , encoding = 'utf-8')
    sp = binascii.b2a_hex(rsa.encrypt(message , key))
    #=======================��¼=======================
����
����#param���Ǽ������ĵĵ�½post��������������õ������ɸ������һ����ȡ�������ݣ���˵�Ĳ���
    param = {'entry' : 'weibo' , 'gateway' : 1 , 'from' : '' , 'savestate' : 7 , 'useticket' : 1 , 'pagerefer' : 'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D' , 'vsnf' : 1 , 'su' : su , 'service' : 'miniblog' , 'servertime' : servertime , 'nonce' : nonce , 'pwencode' : 'rsa2' , 'rsakv' : rsakv , 'sp' : sp , 'sr' : '1680*1050' ,
             'encoding' : 'UTF-8' , 'prelt' : 961 , 'url' : 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack'}
����# �������ʹ��postData��Ψһһ����Ҳ�ܼ�
    s = postData('http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)' , param)
����# ���ˣ�����Ĵ���ִ�е�����ʱ���Ѿ�����˴󲿷��ˣ������кܶ�����ͯЬ����һ�����������������������������ֱ��ȥִ�л�ȡ��˿���⼸�д�����ͻᷢ�����ȡ�ĵ����������½��ҳ�棬�����ư����Ҿ��������ﳤ��һ�찡
����# ���ˣ����ǻ��Ǽ��������urll�ǵ�½֮�����˷��ص�һ�νű��ж����һ����һ����½��url��֮ǰ�����ǻ�ȡ��������֤֮��ģ���һ�����������ĵ�½�������㻹��Ҫ��һ�ΰ����urll��ȡ������get��½����

    urll = re.findall("location.replace\(\'(.*?)\'\);" , s)[0]
    getData(urll)
    #======================��ȡ��˿====================
����# �����û�������ղ��Ǹ�urll��������Ļ�����ô��ϲ�㣡��ɹ��ˣ�������������������΢���ﳩ����ʱ���ˣ���ȡ���κ������ȡ���������ˣ�
����# ���Գ����Ż�ȡ���Լ���΢����ҳ��������ͻᷢ������һ����󼸰�kb���ļ���
    text = getData('http://weibo.com/527891819/home?wvr=5&lf=reg')
    fp = open('yeah.txt' , 'w' , encoding = 'utf-8')
    fp.write(text)
    fp.close()


login_weibo('' , '���΢������')
