import os
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import email
import time
import logging

log = logging.getLogger("O2batch")
log.setLevel(logging.DEBUG)
fh = logging.FileHandler(r"C:\mongo\source\reportlog.txt")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
log.addHandler(fh)

def sendmail(send_to,dt):
    msg = MIMEText("""Dear All,

o2_report_data.csv is not update today
please login in and check it

Thanks,
""" )
    msg['From'] = 'o2@cloud-88.com'
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "FTP not updated"
    smtp = smtplib.SMTP("mail.cloud-88.com")
    smtp.login('o2@cloud-88.com','o2cloud88')
    smtp.sendmail('o2@cloud-88.com',send_to,msg.as_string())
    smtp.close()
if __name__ == "__main__":
    upfile = r"F:\SFTP\o2user1\SPVI_Data_Reporting\o2_report_data.csv"
    stinfo = os.stat(upfile)
    if time.time() - stinfo.st_mtime > 86400:
        print "file not updated"
        sendmail([
                  "august@cloud-88.com",
                  # "bruce@cloud-88.com",
        sys.exit()
    else:
        log.debug("check file")
        pass
    
