from selenium import webdriver
from getpass import getpass
from time import sleep

usr = input("Enter your username or Email: ")
pwd = getpass("Enter your password: ") #getpass() will help your password remain hidden
image_path = input("Please enter your image path: ")

driver =webdriver.Firefox() # or Firefox() if using firefox
driver.get("https://twitter.com/login")

username_box = driver.find_element_by_class_name("js-username-field")
username_box.send_keys(usr)
sleep(3)

password_box = driver.find_element_by_class_name("js-password-field")
password_box.send_keys(pwd)
sleep(3)

login_btn = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
login_btn.submit() # clicking instead of entering a value
sleep(3)

image_box = driver.find_element_by_css_selector("input.file-input.js-tooltip")
image_box.send_keys(image_path)
sleep(3)

tweet_button = driver.find_element_by_css_selector("button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn")
tweet_button.click()