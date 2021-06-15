from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd
import requests
import time
import json
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Crawler(object):

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1890,1080")
        self.driver = webdriver.Chrome(".\chromedriver.exe",chrome_options=chrome_options)
        self.url = "http://firewatchvn.kiemlam.org.vn/#"
        self.delay = 2.2

    def take_data(self,browser,listTinh):
        t = 2
        while True:
            browser.find_element_by_css_selector('div#fw-tinh > div.dropdown-toggle').click()
            time.sleep(0.1)
            try:
                tinh = browser.find_element_by_link_text('#ul-diaphuong-tinh > li:nth-child({}) > a'.format(t))
                if tinh.text in listTinh:
                    print('Chon: '+tinh.text)
                    tinh.click()
                    time.sleep(self.delay)

                    # listHuyen = browser.find_elements_by_css_selector('#tb-view-dp > tbody > tr > td:nth-child(2)')
                    # listHuyen = [x.text for x in listHuyen]
                    # print(listHuyen)
                    # h = 2
                    # while True:
                    #     browser.find_element_by_css_selector('div#fw-huyen > div.dropdown-toggle').click()
                    #     time.sleep(0.1)
                    #     try:
                    #         huyen = browser.find_element_by_css_selector('#ul-diaphuong-huyen > li:nth-child({}) > a'.format(h))
                    #         if huyen.text in listHuyen:
                    #             print('Chon: '+huyen.text)
                    #             huyen.click()
                    #             time.sleep(self.delay)

                    #             x = 2
                    #             while True:
                    #                 browser.find_element_by_css_selector('div#fw-xa > div.dropdown-toggle').click()
                    #                 time.sleep(0.1)
                    #                 try:
                    #                     xa = browser.find_element_by_css_selector('#ul-diaphuong-xa > li:nth-child({}) > a'.format(x))
                    #                     print(xa.text)
                    #                     xa.click()

                    #                     browser.find_element_by_css_selector('#bt-dp-search').click()
                    #                     time.sleep(5)
                    #                 except:
                    #                     break
                    #                 x += 1
                    #         else:
                    #             print('Loai: '+huyen.text)
                    #     except:
                    #         break
                    #     h += 1
                else:
                    print('Loai: '+tinh.text)
            except:
                break
            t += 1
    
    def load_page(self):
        browser = self.driver

        dateStart = datetime.datetime(2020,8,12)
        dateEnd = datetime.datetime(2020,1,1)
        while True:
            browser.get(self.url)
            time.sleep(self.delay)
            searchButoon = browser.find_element_by_css_selector('a[href="#tracuu"]')
            searchButoon.click()
            time.sleep(self.delay)

            browser.find_element_by_id('fw-from-date').clear()
            browser.find_element_by_id('fw-from-date').send_keys(str(dateStart.strftime("%d/%m/%Y")))
            time.sleep(1.5)
            browser.find_element_by_id('fw-to-date').clear()
            browser.find_element_by_id('fw-to-date').send_keys(str(dateStart.strftime("%d/%m/%Y")))
            time.sleep(1.5)
            print(dateStart.strftime("%d/%m/%Y")) 

            browser.find_element_by_css_selector('div#fw-tinh > div.dropdown-toggle').click()
            time.sleep(self.delay)
            tinh = browser.find_element_by_css_selector('#ul-diaphuong-tinh > li:nth-child(1)')
            tinh.click()
            time.sleep(self.delay)

            browser.find_element_by_css_selector('#bt-dp-search').click()
            time.sleep(3)
            listTinh = browser.find_elements_by_css_selector('#tb-view-dp > tbody > tr > td:nth-child(2)')
            listTinh = [x.text for x in listTinh]
            if len(listTinh) != 0:
                print(listTinh)
                self.take_data(browser,listTinh)
            if dateStart <= dateEnd:
                break 
            dateStart -= datetime.timedelta(days=1)

    def close_browser(self):
        self.driver.close()
        print('Done!')

if __name__ == "__main__":
    # crawl
    sarcasm_crawler = Crawler()
    sarcasm_crawler.load_page()
    sarcasm_crawler.close_browser()
