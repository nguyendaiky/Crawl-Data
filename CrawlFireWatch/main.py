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
        self.delay = 2

    def take_data(self,browser,date,listTinh):
        for t in range(len(listTinh)):
            line = {}
            line['Ngay'] = date
            browser.find_element_by_css_selector('div#fw-tinh > div.dropdown-toggle').click()
            time.sleep(0.3)
            tinh = browser.find_element_by_link_text(listTinh[t])
            time.sleep(0.3)
            print(tinh.text)
            line['Tinh'] = tinh.text
            tinh.click()
            time.sleep(self.delay)

            listHuyen = browser.find_elements_by_css_selector('#tb-view-dp > tbody > tr > td:nth-child(2)')
            listHuyen = [x.text for x in listHuyen]
            print(listHuyen)
            time.sleep(self.delay)
            for h in range(len(listHuyen)):
                browser.find_element_by_css_selector('div#fw-huyen > div.dropdown-toggle').click()
                time.sleep(0.3)
                huyen = browser.find_element_by_link_text(listHuyen[h])
                time.sleep(0.3)
                print(huyen.text)
                line['Huyen'] = huyen.text
                huyen.click()
                time.sleep(self.delay)

                listXa = browser.find_elements_by_css_selector('#tb-view-dp > tbody > tr > td:nth-child(2)')
                listXa = [x.text for x in listXa]
                print(listXa)
                time.sleep(self.delay)
                for x in range(len(listXa)):
                    browser.find_element_by_css_selector('div#fw-xa > div.dropdown-toggle').click()
                    time.sleep(0.3)
                    xa = browser.find_element_by_link_text(listXa[x])
                    time.sleep(0.3)
                    print(xa.text)
                    line['Xa'] = xa.text
                    xa.click()
                    time.sleep(self.delay)

                    listKinhDo = browser.find_elements_by_css_selector('#tb-view-dp > tbody > tr > td:nth-child(2)')
                    listKinhDo = [x.text for x in listKinhDo]
                    listViDo = browser.find_elements_by_css_selector('#tb-view-dp > tbody > tr > td:nth-child(3)')
                    listViDo = [x.text for x in listViDo]
                    for i in range(len(listKinhDo)):
                        print((listKinhDo[i],listViDo[i]))
                        data = line.copy()
                        data['Kinh Do'] = listKinhDo[i]
                        data['Vi Do'] = listViDo[i]
                        with open('Data.txt','a') as f:
                            json.dump(data,f)
                            f.write('\n')

    def load_page(self):
        browser = self.driver
        browser.implicitly_wait(10)

        dateStart = datetime.datetime(2020,5,13)
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
                self.take_data(browser,dateStart.strftime("%d/%m/%Y"),listTinh)
            if dateStart <= dateEnd:
                break 
            dateStart -= datetime.timedelta(days=1)

    def close_browser(self):
        self.driver.close()
        print('Done!')

def convert_to_csv(path):
    with open(path,'rb') as f:
        data = f.readlines()
    data = map(lambda x: x.rstrip(),data)
    data_json_string = b'[' + b','.join(data) + b']'
    data_df = pd.read_json(data_json_string)
    print(data_df.head(10))
    data_df.to_csv(path[:-3]+'csv')

if __name__ == "__main__":
    # crawl
    sarcasm_crawler = Crawler()
    sarcasm_crawler.load_page()
    sarcasm_crawler.close_browser()