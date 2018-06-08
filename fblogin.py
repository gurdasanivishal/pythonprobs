#!/usr/bin/python
import unittest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import os
#import webbrowser 
from getpass import getpass

#input email and password
#getpass function is use to enter password in hidden mode 
usr=input('Enter Email Id :')
pwd=getpass('Enter Password:')
 
#open firefox and goto facebook login page
driver = webdriver.Firefox()
driver.get('https://facebook.com')

#automatically fill enrey of email and password
username_box = driver.find_element_by_id("email")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(pwd)

login_bnt= driver.find_element_by_id("u_0_2")
login_bnt.submit()
