from db import store_data,load_data,TASKS_DB,reply_msg
import os
from whatsapp import whatsappui


class Arvi(whatsappui,load_data):

    def __init__(self):
        os.system("taskkill /f /im  chrome.exe")
        os.system("taskkill /f /im  chromedriver.exe")
        load_data.__init__(self)
        whatsappui.__init__(self)
        self.search_click('Arvi')

    def do_task(self,taskname):
        task={
        'click_pic':self.click_pic,
        'send_test_mail' : self.send_email,
        'send_mail_confirm':self.send_mail_all ,
        'add_address':self.add_address,
        'msg_to':self.msg_other
        }
        if type(taskname) is not str:
            to_do = taskname[0]
            args = taskname[1:]
            task.get(to_do)(args)
        else:
            task.get(taskname)()

if __name__=="__main__":
    handle=Arvi()
    msg='go online'
    while True and msg.lower() !="go offline":
        msg=handle.read_msg()
        r_msg=reply_msg(msg)
        if r_msg[0]:
            handle.do_task(r_msg[1])
        else:
            handle.write_msg(r_msg[1])

