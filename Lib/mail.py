#sending email from python       @@
import smtplib


message = """\
Subject: {}

{}
"""

class send_email():

    def __init__(self,email_host='smtp.gmail.com',email_port=465):
        self.emailObj=smtplib.SMTP_SSL(email_host,email_port)
        self.emailObj.ehlo()

    def login(self,username,password):
        self.emailObj.login(username,password)

    def send_mail(self,from_mail_id,to_mail_id,subject,email_body):
        self.emailObj.sendmail(from_mail_id,to_mail_id,
            message.format(subject,email_body))
        print(from_mail_id,to_mail_id,
            message.format(subject,email_body))
        return True

    def quit(self):
        self.emailObj.quit()



if __name__=='__main__':

    username = 'aravinthbalajee1996@gmail.com'
    to= 'aravinth.balajee@gmail.com'
    pwd= 'KENDRIYAVIDYALAYA'
    subject = 'Python Training'
    body='''
    Hi {},

    Welcome to Python Training!!
    I hope you find it fun and use it daily.

    Regards,
    Aravinth Balajee R
    '''
    mail=send_email()
    mail.login(username,pwd)
    mail.send_mail(username,to,subject,body.format('Arvi'))
    mail.quit()


