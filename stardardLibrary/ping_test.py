# coding=utf-8

import os
import datetime
import msvcrt
# import smtplib
# from email.MIMEText import MIMEText
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEBase import MIMEBase
# from email.Utils import formatdate, COMASPACE
# from email import Encoders

ips = ['121.14.106.149',
        '96.38.213.6',
        '192.168.2.12',
        ]

# def sendtext(msg):
#     msg = MIMEText(msg) # 构造文本类型的邮件
#     # 构造邮件头
#     msg['from'] = 'august@cloud-88.com'
#     msg['To'] = '1927064778@qq.com'
#     msg['Subject'] = 'ping debugs'
#     msg['Date'] = formatdate(localtime=True)
#     text = MIMEText('欢迎来到ttoo','plain','utf-8')
#     msg.attach(text)
#     # server
#     server = smtplib.SMTP('mail.cloud-88.com')
#     server.login('august@cloud-88.com', 'august')
#     server.sendmail('august@cloud-88.com', '1927064778@qq.com', msg.as_string())
#     server.quit()

# def sendpart(sendto):
#     msg = MIMEMultipart() # 构造带附件类型邮件
#     # 构造邮件头
#     msg['From'] = 'august@cloud-88.com'
#     msg['To'] = COMASPACE.join(sendto)
#     msg['Subject'] = 'ping debug.log'
#     msg['Date'] = formatdate(localtime=True)
#     text = MIMEText('欢迎来到这里...')
#     # msg.attach(text)
#     # 构造附件
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(open('debug.log', 'rb').read())
#     Encoders.encode_base64(part)
#     part.add_header("Content-Disposition","attachment;filename=%s" % os.path.abspath('debug.log')
#     msg.attach(part)
#     # smtp
#     server = smtplib.SMTP('mail.cloud-88.com')
#     server.login('august@cloud-88.com', 'august')
#     server.sendmail('august@cloud-88.com',sendto,msg.as_string())
#     smtp.quit()
print 'ping...start...'
for ip in ips:
    dealping = 'ping ' + ip + ' >> ping.log'
    ping = os.system(dealping)
    str1 = ''
    if not ping:
        continue
    else:
        now = datetime.datetime.now()
        str_time = r'{0}:{1}:{2} {3}-{4}-{5} '.format(now.hour,now.minute,now.second,now.month,now.day,now.year)
        with open('debug.log','a+') as fp:
            str1 = str_time + ip + ' is down' + '\n'
            fp.write(str1)

    print(str1+'please enter a key to exit')
    msvcrt.getch()
        # sendpart(['1927064778@qq.com','872781095@qq.com'])
        # sendtext(str1)
