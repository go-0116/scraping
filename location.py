from logging import exception
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.keys import Keys
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")

df = pd.read_csv('tokyo.csv', encoding="shift_jis")
location_list = df['town']

browser = webdriver.Chrome(executable_path='/home/gm116/bin/chromedriver',options=chrome_options)
url = 'https://www.ubereats.com/jp/feed?mod=deliveryDetails&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVCOCU4QiVFOCVCMCVCNyVFNSU4QyVCQSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUowUWd4NjdLTUdHQVJkMlpiT2JMWkhQRSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS42NjE5NzA3JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjcwMzc5NSU3RA%3D%3D&ps=1'

URL = []

for location in location_list[range(5)]:
    browser.get(url)
    change_element = browser.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/a')
    change_element.click() #配送先クリック

    location_element = browser.find_element_by_xpath('//*[@id="location-typeahead-location-manager-input"]')
    location_element.send_keys(location)
    sleep(1)
    location_element.send_keys(Keys.ENTER)
    sleep(1)
    URL.append(browser.current_url)

df['urls'] = URL
print(df)