from selenium import webdriver
from getpass import getpass

usr = input("Enter your username or Email: ")
pwd = getpass("Enter your password: ") #getpass() will help your password remain hidden

driver =webdriver.Chrome() # or Firefox() if using firefox
driver.get("https://www.facebook.com/")

username_box = driver.find_element_by_id("email")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id("u_0_3")
login_btn.submit() # clicking instead of entering a value