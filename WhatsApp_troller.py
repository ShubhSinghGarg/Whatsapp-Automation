from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Shubh Singh Garg\\Desktop\\New folder (2)\\Added libs and drivers\\drivers\\chromedriver.exe")
driver.get ("https://web.whatsapp.com/")

userName = input('Enter the name of the user or the group: ')

input("Press a key after logging into whatsapp")

reciver = driver.find_element_by_xpath('//span[@title = "{}"]'.format(userName))
reciver.click()

msg_box = driver.find_element_by_class_name('_3uMse')

time.sleep(2)
with open("troll.txt") as text:
    lines = text.readlines()

for msg in lines:
    msg_box.send_keys(msg)
#    time.sleep(0.5)

submit = driver.find_element_by_class_name('_1U1xa')
submit.click()