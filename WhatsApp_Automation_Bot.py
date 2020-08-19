from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Shubh Singh Garg\\Desktop\\New folder (2)\\Added libs and drivers\\drivers\\chromedriver.exe")
driver.get ("https://web.whatsapp.com/")

userName = input('Enter the name of the user or the group: ')
msg = input("Enter the message you want to deliver ")
count = int(input("How many time would you like to repeat the message: "))

input("Press a key after logging into whatsapp")

reciver = driver.find_element_by_xpath('//span[@title = "{}"]'.format(userName))
reciver.click()

msg_box = driver.find_element_by_class_name('_3uMse')

for i in range(count):
    msg_box.send_keys(msg)
    submit = driver.find_element_by_class_name('_1U1xa')
    submit.click()