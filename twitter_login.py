from selenium import webdriver
from getpass import getpass

usr = input("Enter your username or Email: ")
pwd = getpass("Enter your password: ") #getpass() will help your password remain hidden

driver =webdriver.Firefox() # or Firefox() if using firefox
driver.get("https://twitter.com/login")

username_box = driver.find_element_by_class_name("js-username-field")
username_box.send_keys(usr)

password_box = driver.find_element_by_class_name("js-password-field")
password_box.send_keys(pwd)

login_btn = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
login_btn.submit() # clicking instead of entering a value