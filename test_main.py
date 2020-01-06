from Lib import whatsapp
from selenium import webdriver
import os
if __name__=='__main__':
    print os.getcwd()
    chromedriver=(os.getcwd())+r'\chromedriver.exe'
    print chromedriver
    Driver=webdriver.Chrome(chromedriver)
    Driver.get('https://www.google.co.in/')
    Driver.maximize_window()

