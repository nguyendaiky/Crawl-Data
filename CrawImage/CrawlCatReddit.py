from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver.chrome.options import Options

import os
import wget
import time

ext_file1 = r"C:\Users\Nguyen Dai Ky\AppData\Local\Google\Chrome\User Data\Default\Extensions\bgnkhhnnamicmpeenaelnjfhikgbkllg\3.5.34_0.crx"
ext_file2 = r"C:\Users\Nguyen Dai Ky\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.35.2_0.crx"
ext_file3 = r"C:\Users\Nguyen Dai Ky\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.10.2_0.crx"
# remove popup
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_extension(ext_file1)
chrome_options.add_extension(ext_file2)
chrome_options.add_extension(ext_file3)

# setup driver and get url
driver = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe',chrome_options=chrome_options)
driver.create_options()
driver.get('https://www.reddit.com/r/cat/')

# scroll and get img
n_scrolls = 10
for i in range(1,n_scrolls):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)

    # img = driver.find_elements_by_xpath("//img[contains(@class,'ImageBox-image') and contains(@alt, 'Post image')]")
    img = driver.find_elements_by_css_selector("img.ImageBox-image.media-element")
    images = [i.get_attribute('src') for i in img]

# save img
path = os.getcwd()
path = os.path.join(path, 'cats')
os.mkdir(path) 

counter = 1
for img in images:
    if counter == 201:
        break
    save_as = os.path.join(path, 'cat' + str(counter) + '.jpg')
    wget.download(img, save_as)
    time.sleep(1)
    counter += 1

driver.close()
print('done!')
