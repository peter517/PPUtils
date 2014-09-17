from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib
import sys

class STMPEmailSender:
    
    stmp_ssl_ = smtplib.SMTP_SSL()
    stmp_ssl_port_ = 465;
    
    def __init__(self):
        print "init email sender"
        
    def connect(self,mail_host,mail_user,mail_pwd):
        print "start connect email server"
        self.stmp_ssl_.set_debuglevel(1)
        self.stmp_ssl_.connect(mail_host,self.stmp_ssl_port_)
        self.stmp_ssl_.login(mail_user,mail_pwd)
        print "finsh connect email server"
        
    def disconnect(self):  
        self.stmp_ssl_.close()
        
    def send(self,mail_user,mail_to,mail_subject,mail_content,mail_attach_filename = None):
        
        print "start send email"
        try:
     
            mail_msg = MIMEMultipart()
        
            if mail_attach_filename is not None:
                attach = MIMEText(open(mail_attach_filename,'rb').read(),'base64','gb2312')
                attach["Content-Type"] = 'application/octet-stream'
                attach["Content-Disposition"] = 'attachement;filename = ' + mail_attach_filename
                mail_msg.attach(attach)
        
            mail_msg.attach(MIMEText(mail_content))
            mail_msg['To'] = ', '.join(mail_to)
            mail_msg['from'] = mail_user
            mail_msg['subject'] = mail_subject
            
            self.stmp_ssl_.sendmail(mail_user,mail_to,mail_msg.as_string())
        
            print "send email sucuess"
        except Exception,e:
            print e

def read_file_to_str(filename):
    line_list = open(filename).readlines()
    line_str = ""
    for line in line_list:
        line_str += line;
    return line_str;

def read_file_to_list(filename):
    return open(filename).readlines()

if __name__ == '__main__' :
    
    if len(sys.argv) != 4:
        print "arg len is not 4, exit"
        sys.exit()
    
    mail_host = sys.argv[1]
    mail_user = sys.argv[2]
    mail_pwd = sys.argv[3]
    
    mail_to_filename = "mail_to.txt"
    mail_to = read_file_to_list(mail_to_filename);
    
    mail_subject = "Mmpc Sdk Auto Build Error"
     
    mail_content_filename = "build_error.log"
    mail_content = read_file_to_str(mail_content_filename)
    
    mail_attach_filename = "build.log"
    
    emailSender = STMPEmailSender();
    emailSender.connect(mail_host, mail_user, mail_pwd)
    emailSender.send(mail_user, mail_to, mail_subject, mail_content, mail_attach_filename)
    emailSender.disconnect()
