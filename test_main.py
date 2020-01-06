from Lib.arvi_tasks import Arvi,reply_msg

def run():
    handle=Arvi()
    msg='go online'
    while True and msg.lower() !="go offline":
        msg=handle.read_msg()
        r_msg=reply_msg(msg)
        if r_msg[0]:
            handle.do_task(r_msg[1])
        else:
            handle.write_msg(r_msg[1])


if __name__=='__main__':
    run()



