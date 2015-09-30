# encoding=utf-8

from fabric.api import *
from fabric.network import *
from fabric.colors import *

# 用法 pip install fabric
# fab pwd
# env.user = 'leon'
# env.password = ''
# env.hosts = ['96.38.213.2',]

# env.roledefs = {
#             'host1': ['leon@69.61.83.181:22',],
#             'realserver': ['user2@host2:port2', ]
#             }
env.hosts = [
    'leon@69.61.83.181:22',
    # 'adminuser@192.168.0.119:22',
]
env.passwords = {
    'leon@69.61.83.181:22': '',
    # 'adminuser@192.168.0.119:22': 'adminuser',
}


@task
def pwd():
    with cd('~'):  # cd/lcd/hide/quiet/path
        # sudo/get/put/local/prompt/open_shell/reboot
        out = run('cat /etc/shadow')
        # print(out.succeeded/failed/return_code)


@task
def git():
    print(green(u'开始china car service git update...'))
    with cd('~/backup/gaeccsbookings/'):
        out = run('git pull')
        if out.return_code == 0:
            print(cyan(u'更新git完成...'))
