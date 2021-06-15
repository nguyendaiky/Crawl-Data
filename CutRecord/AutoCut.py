from selenium import webdriver
import time
import os

url = "https://audiotrimmer.com/"
browser = webdriver.Chrome(r'.\Prepare-file\chromedriver.exe')
browser.get(url)

time.sleep(2)
fileInput = browser.find_element_by_css_selector('#input')
fileInput.send_keys(os.getcwd()+'\Source\Test1_01.mp3')
time.sleep(1)