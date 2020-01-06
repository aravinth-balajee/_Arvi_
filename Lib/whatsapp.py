from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import mail
import socket

"""
GLOBAL VARIABLES
"""
WHATSAPP_URL='https://web.whatsapp.com/'
X_SEARCH_BAR= '//*[(@title="Search or start new chat")] '
X_ARVI_='//span[contains(@title,"_name_")]/em'
X_MSG_BOX=   '//*[contains(text(),"Type a message")] '
X_READ_MSG='//*[(@class="copyable-text")] '
X_PIN= '//*[(@title="Attach")] '
X_FILE= '//input[(@accept="*")]'
X_F_SEND='//*[@data-icon="send-light"]'
X_CAMERA='//*[@data-icon="camera"]'
X_CLICK='//*[@data-icon="camera-light"]'

email_list =[
'dpandu.iisc@gmail.com',
'kaja.sana@gmail.com',
'c.kumaraguru@gmail.com',
'ors.abinaya@gmail.com' ,
'2020.archana@gmail.com'  ,
'praisyjones@gmail.com'   ,
'preethask2810@gmail.com'   ,
'baskarb.srutinanda@gmail.com' ,
'arunsinghrasaputhra@gmail.com'   ,
'pmeiyarasu10@gmail.com'      ,
'bharatharunp@gmail.com',
'aravinth.balajee@gmail.com'
]

temp_list =[
'aravinth.balajee@gmail.com',
'aravinthbalaji12@gmail.com' ,
'aravperry@gmail.com'
]

def wait_till(driver,xpath):
    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        driver.implicitly_wait(2)
        return True
    except:
        pass
    return

def internet_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        print 'Internet connecting..'
        socket.create_connection(("www.google.com", 80))
        print 'Internet connected'
        return True
    except OSError:
        pass
    return False


class whatsappui():

    def __init__(self):
        self.connected = False
        if internet_connected():
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=C:\Users\Aravinth Balajee\AppData\Local\Google\Chrome\User Data")
            options.add_argument("start-maximized")
            options.add_argument("--disable-extensions")
            ##options.add_argument("--headless")
            ##options.add_argument("--window-size=1366,768")
            ##options.binary_location=r"C:\Users\Aravinth Balajee\AppData\Local\Google\Chrome SxS\Application\chrome.exe"
            driver = webdriver.Chrome(r'D:\_AravinthBalajee\Depreciated\Hobbies\Project\_Arvi_\chromedriver.exe',chrome_options=options)
            driver.implicitly_wait(2)
            driver.get(WHATSAPP_URL)
            if wait_till(driver,X_SEARCH_BAR):
                self.connected = True
            ##options.add_argument("--headless")
            ##options.add_argument("--window-size=1366,768")
            ##options.binary_location=r"C:\Users\Aravinth Balajee\AppData\Local\Google\Chrome SxS\Application\chrome.exe"            
            ##        driver.minimize_window()
            ##        driver.maximize_window()
            ##        driver.save_screenshot(r'C:\Users\Aravinth Balajee\Desktop\Project\test.png')
            self.driver=driver

        self.username = 'aravinthbalajee1996@gmail.com'
        self.pwd= 'KENDRIYAVIDYALAYA'
        self.body='''
        Hi {},

        Welcome to Python Training!!
        I hope you find it fun and use it daily.

        Regards,
        Aravinth Balajee R
        '''

    def search_click(self,name):

        driver=self.driver
        SearchStatus=driver.find_element_by_xpath(X_SEARCH_BAR)
        SearchStatus.click()
        SearchStatus.clear()
        SearchStatus.send_keys(name)
        X_name_=X_ARVI_.replace("_name_",name)
        wait_till(driver,X_name_)
        driver.find_element_by_xpath(X_name_).click()
        self.driver=driver

    def write_msg(self,msg,others=False):

        driver=self.driver
        wait_till(driver,X_MSG_BOX)
        sleep(1)
        SearchS=driver.find_element_by_xpath(X_MSG_BOX).find_element_by_xpath('..')
        SearchS.click()
        if others:
            SearchS.send_keys((msg)+"\n")
        else:
            SearchS.send_keys("*Arvi:* {}".format(msg)+"\n")
        self.driver=driver
        print ""

    def read_msg(self) :

        driver=self.driver
        wait_till(driver,X_READ_MSG)
        while True:
            SearchS=driver.find_elements_by_xpath(X_READ_MSG)
            if "Arvi:" not in SearchS[-1].text:
                task=SearchS[-1].text
                return task
        self.driver=driver

    def msg_other(self,argums):
        person_name,msg= argums
        self.search_click(person_name)
        self.write_msg(msg,others=True)
        self.search_click('Arvi')
        self.write_msg('Your Message Sent')

    def send_files(self,media_path):
        try:
            driver=self.driver
            driver.find_element_by_xpath(X_PIN).click()
            mediaclass=driver.find_element_by_xpath(X_FILE)
            driver.execute_script("arguments[0].style='display: true';", mediaclass)
            mediaclass.send_keys(media_path)
            wait_till(driver,X_F_SEND)
            driver.find_element_by_xpath(X_F_SEND).click()
            self.write_msg("Media sent")
            self.driver=driver
        except Exception as err:
            print err

    def click_pic(self):

        driver=self.driver
##        driver.maximize_window()
        driver.find_element_by_xpath(X_PIN).click()
        sleep(1)
        camclass=driver.find_element_by_xpath(X_CAMERA)
        camclass.find_element_by_xpath('..').click()
        sleep(1)
        driver.find_element_by_xpath(X_CLICK).click()
        wait_till(driver,X_F_SEND)
        driver.find_element_by_xpath(X_F_SEND).click()
        self.write_msg("Picture sent")
        self.driver=driver

    def send_email(self):
        self.email = mail.send_email()
        self.email.login(self.username,self.pwd)
        for people in temp_list:
            usr=people.split('@')[0]
            self.email.send_mail(self.username,people,'Python Training',self.body.format(usr))
            self.write_msg('Mail sent to {}'.format(usr))
        self.write_msg('All Mail Sent')
        self.email.quit()

    def send_mail_all(self):
        self.email = mail.send_email()
        self.email.login(self.username,self.pwd)
        for people in email_list:
            usr=people.split('@')[0]
            self.email.send_mail(self.username,people,'Python Training',self.body.format(usr))
            self.write_msg('Mail sent to {}'.format(usr))
        self.write_msg('All Mail Sent')
        self.email.quit()

    def add_address(self,mailid):
        temp_list.append(mailid)
        email_list.append(mailid)
        self.write_msg('Mail List updated {}'.format(email_list))





if __name__=='__main__' :
    handle=whatsappui()
    handle.search_click("_Arvi_")
    handle.click_pic()


