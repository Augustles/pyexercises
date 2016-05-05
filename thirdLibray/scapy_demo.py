# encoding=utf-8

from scapy.all import *
from scapy.all import rdpcap

pkts = rdpcap('abc.pcap')


packet = IP()  # 创建一个封包
packet.show()  # 显示封包资讯
packet.src  # 显示封包来源地
packet.ttl  # 输出封包ttl, 64


# scapy
sudo scapy  # root用户启动scapy
pkts = sniff(iface='eth0', count=5)  # 网络eth0接口, 5个数据包
# 常用还有filter过滤协议, icmp, tcp/udp, http
pkts[0]  # 显示数据包概况
pkts[0].show()  # 显示详情
hexdump(pkts[0])  # 16进制形式显示
wrpcap('demo.pcap', pkts)  # 写入到demo.pcap
read = rdpcap('demo.pcap')  # 读取demo.pcap
s = str(pkts[0])  # 转化为str
recon = Ether(s)  # 重构数据包
export_object(s)  # 导出base64对象
new = import_object()  # 导入base64对象, 输入完成后(ctrl+D)


# 获取内网mac地址
# ipscan = "192.168.0.1/24"

# try:
#     ans, unans = srp(
#         Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=ipscan), timeout=2, verbose=False)
# except Exception, e:
#     print str(e)
# else:
#     for snd, rcv in ans:
#         list_mac = rcv.sprintf("%Ether.src% - %ARP.psrc%")
#         print list_mac


from scapy.all import *
import scapy_http.http  # pip install scapy-http


# console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
T = '\033[93m'  # tan

interface = 'eth0'

d = []


def cap(p):
    if p.haslayer('HTTP'):
        try:
            url = p['HTTP'].Host + ' => ' + p['HTTP'].Path
            if url not in d and p['HTTP'].Method == 'GET':
                d.append(url)
                print p['HTTP'].Method, url
        except:
            pass

sniff(prn=cap, store=0)
