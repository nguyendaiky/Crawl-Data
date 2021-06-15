from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# read VideoList.txt and ViewCount.txt
videoList = open('VideoList1.txt')
videos = videoList.readlines()
videoList.close()
viewCountFile = open('ViewCount.txt','r')
viewCount = int(viewCountFile.read())
viewCountFile.close()

NUMBER_OF_WINDOW = 1
NUMBER_OF_VIDEO = len(videos)
LOOP_TIME = 252

videoIndex = 0
windowIndex = 0
windowCount = 1

# add extension
chrome_options = Options()
chrome_options.add_extension(r'prepare-file\3.5.34_0.crx')

# open browser
browser = webdriver.Chrome('prepare-file\chromedriver.exe',chrome_options=chrome_options)
browser.get(videos[videoIndex])

# click play button
time.sleep(2)
playButton = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')
playButton.click()
time.sleep(1)

# time.sleep(10)
# time_duration = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration')
# print(time_duration.text)

# loop 
while True:
    videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO
    windowIndex = (windowIndex + 1) % NUMBER_OF_WINDOW
    print('Tab '+str(windowIndex)+' : video '+str(videoIndex))
    url = videos[videoIndex].strip()

    if windowCount < NUMBER_OF_WINDOW:
        browser.execute_script('window.open("'+url+'")')
        windowCount += 1
    else:
        browser.switch_to.window(browser.window_handles[windowIndex])
        time.sleep(1)
        browser.get(url)

    viewCount += 1
    viewCountFile = open('ViewCount.txt', 'w')
    viewCountFile.write(str(viewCount))
    viewCountFile.close()

    time.sleep(LOOP_TIME)








