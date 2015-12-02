import config
import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText

class Email:

    def __init__(self,to,cc,bcc,log):
        
        self.sender  = config.email_sender
        self.to      = to
        self.cc      = cc
        self.bcc     = bcc

        self.msg = MIMEMultipart()

        self.log = log
        
    def message(self,mes):
        txt = MIMEText(mes)
        self.msg.attach(txt)


    def send(self,subject):

        self.msg['Subject'] = subject
        self.msg['From']    = self.sender
        self.msg['To']      = ",".join(self.to)
        
        self.msg['Cc']      = ",".join(self.cc)
        self.msg['Bcc']     = ",".join(self.bcc)

        s = None
        self.log.debug("Opening socket to send.columbia.edu.")
        try :
            s = smtplib.SMTP_SSL("send.columbia.edu",465)
        except smptlib.SMTPException:
            self.log.exception("SMPT Connection error")
            sys.exit(1)

        self.log.debug("Logging in with %s" % config.email_user)
        try:       
            s.login(config.email_user,config.email_pass)
        except smptlib.SMTPException:
            self.log.exception("Bad Authentication")
            sys.exit(1)

        self.log.debug("Sending mail")
        try:
            s.sendmail(self.sender,self.to + self.cc + self.bcc,self.msg.as_string())
        except:
            self.log.exception("Unable to send message")
            sys.exit(1)

        self.log.debug("Mail sent, quitting.")
        s.quit()
