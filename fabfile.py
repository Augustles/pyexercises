# encoding=utf-8

from fabric.api import *
from fabric.network import *

# 用法 pip install fabric
# fab pwd
# env.user = 'leon'
# env.password = '$wB2ZjWmofg'
# env.hosts = ['96.38.213.2',]

# env.roledefs = {
#             'host1': ['leon@96.38.213.2:22',],  
#             'realserver': ['user2@host2:port2', ]
#             }
env.hosts = [
    'leon@96.38.213.2:22',
    'adminuser@192.168.0.119:22',
    ]
env.passwords = {
    'leon@96.38.213.2:22': '123456',
    'adminuser@192.168.0.119:22': 'adminuser',
}

@task
def pwd():
    with cd('~'): # cd/lcd/hide/quiet/path
        out = run('cat /etc/shadow') # sudo/get/put/local/prompt/open_shell/reboot
        # print(out.succeeded/failed/return_code)
