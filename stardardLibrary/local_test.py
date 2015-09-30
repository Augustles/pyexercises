# coding=utf-8

import os
import socket
import getpass
import subprocess
import re
import uuid

hostname = socket.gethostname()
l_ip = socket.gethostbyname(hostname)  # socket.gethostbyname_ex()
username = getpass.getuser()
node = uuid.getnode()
mac = uuid.UUID(int=node)
addr = mac.hex[-12:]
# 处理addr:0030673f69ee
s = ''
for x in range(0, len(addr), 2):
    s += addr[x:x + 2] + '-'
addr = s[:-1]
# if os.name == 'nt':
#     t_bios = os.system('wmic bios get name,SMBIOSBIOSVersion,manufacturer')
#     t_system = os.system('wmic computersystem get Name,workgroup,NumberOfProcessors,manufacturer,Model')
#     t_bootin = os.system('wmic computersystem get SystemStartupOptions')
#     t_startup = os.system('wmic startup get user,command')
#     t_account = os.system('wmic useraccount get name,PasswordRequired,status')
#     t_share = os.system('wmic share get path,status,description')
#     t_os = os.system('wmic os get name,OSArchitecture,MUILanguages')
#     t_disk = os.system('wmic LOGICALDISK get name,Description,filesystem,size,freespace')
#     t_cpu = os.system('wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors')
#     t_process = os.system('wmic process list brief')
#     t_nic = os.system('wmic nic list brief')
# os.system('net view > netview.txt')
# with open('netview.txt', 'r+') as f:
#     for line in f:
#         if line.find('\\') == 0:
#             print line[2:]
#             c_name = line[2:]
#             ping = os.system('ping' + c_name + ' >> ping.txt')

# out = subprocess.check_output('net view')
# out_f = re.findall(r'\\', out)


print hostname, l_ip, addr, username
