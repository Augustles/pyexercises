# coding=utf-8

import telnetlib

def startTelnet(host, username, password, finish, commands):
    '''
    telnet远程登录
    '''
    # 连接telnet服务器
    tn = telnetlib.Telnet(host, port=23, timeout=10)
    tn.set_debuglevel(2)

    # 输入登录帐号密码
    # tn.read_until('(y/n): ')
    # trn.write('y\n')
    tn.read_until('login: ')
    tn.write(username + '\n')
    tn.read_until('password: ')
    tn.write(password + '\n')
    tn.read_until('C:\Users\Administrator>')
    tn.write('dir\n')

    # 登录后执行命令
    # tn.read_until(finish)
    # tn.write('%s\n' % commands)

if __name__ == '__main__':
    # 配置选项
    host = '121.14.106.149'
    username = 'administrator'
    password = '76WqFcjmwfxJTMdV'
    finish = ':~$'
    commands = ['dir']
    startTelnet(host, username, password, finish, commands)
