import pickle
import os
import random

"""
global variables
"""
CACHE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"\cache"
TASKS_DB={"routine":{}}
GRETTINGS=['hi','hey','hello','arvi']

INST_TASKS=['msg_other','eval']
R_GRETTINGS=['How can I help you?','Hi','Hi! How you doing today?','Hi!Nice to have you back']

Actions={'grettings':R_GRETTINGS,'instant_tasks':INST_TASKS}

class load_data():

    def __init__(self):
        global CACHE_PATH,TASKS_DB
        if not os.path.exists(CACHE_PATH+"\user_t_data.dll"):
            taskcache=open(CACHE_PATH+"\user_t_data.dll",'wb')
            pickle.dump(TASKS_DB,taskcache)
            taskcache.close()
        else:
            global CACHE_PATH,TASKS_DB
            taskcache=open(CACHE_PATH+"\user_t_data.dll",'rb')
            TASKS_DB=pickle.load(taskcache)
            taskcache.close()

class store_data():
    def __init__(self):
        global CACHE_PATH,TASKS_DB
        taskcache=open(CACHE_PATH+"\user_t_data.dll",'wb')
        pickle.dump(TASKS_DB,taskcache)
        taskcache.close()


def reply_msg(msg):
    global GRETTINGS,R_GRETTINGS
    if msg.lower() in GRETTINGS:
        return [False,random.choice(R_GRETTINGS)]

    elif "click photo" in msg.lower() or "click pic" in msg.lower():
        return [True,'click_pic']

    elif msg.find(" to ") and msg.find('msg')!=-1:
       result =  'msg_to'
       msg,person=msg.split('msg')[1].split(" to ")
       print [True,[result,person,msg]]
       return [True,[result,person,msg]]

    elif msg.find('cal')!=-1:
        result=eval(msg.split('cal')[1].strip())
        return [False,result]
    elif msg.find('test mail')!=-1:
        result='send_test_mail'
        return [True,result]

    elif msg.find('mail confirm')!=-1:
        result='send_mail_confirm'
        return [True,result]

    elif msg.find('offline')!=-1:
        result='go_offline'
        return [True,result]

    elif msg.find('update mailid')!=-1:
        result='add_address'
        return [True,[result,msg.split('update mailid')[1].strip()]]
    else:
        return [False,"Sorry Iam not Programmed"]














