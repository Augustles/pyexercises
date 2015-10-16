# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import pysftp  # pip install pysftp
from time import sleep

print u' => 正在检查182和149ftp是否正常工作...'
info1 = {'username': 'lendsci',
         'password': 'lendsci', 'port': 22}


def get_sftp_status(info):
    file = 'check.py'
    if os.path.exists(file):
        os.chdir(os.getcwd())
        os.remove(file)
        sleep(0.1)
    try:
        with pysftp.Connection(**info1) as sftp:
            # print sftp.listdir()
            sftp.get('check.py', preserve_mtime=True)
            if os.path.exists(file):
                sftp.remove(file)
                sftp.put(file, preserve_mtime=True)
                if sftp.exists(file):
                    print ' => Good : ' + info + ' is work'
                else:
                    print info + ' upload error'
            else:
                print info + ' dowload error'
    except Exception, e:
        print e

info = info1['host'] = '121.14.106.149'
get_sftp_status(info)
info = info1['host'] = '69.61.83.182'
get_sftp_status(info)


sleep(30)
