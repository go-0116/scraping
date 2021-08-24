from logging import exception
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(executable_path='/home/gm116/bin/chromedriver',options=chrome_options)
url = 'https://www.ubereats.com/jp/feed?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVCOCU4QiVFOCVCMCVCNyVFNSU4QyVCQSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUowUWd4NjdLTUdHQVJkMlpiT2JMWkhQRSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS42NjE5NzA3JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjcwMzc5NSU3RA%3D%3D'
browser.get(url)
sleep(5)
#wait = WebDriverWait(browser, 10)

urls = []
names = []
ids = []
i = 1
url_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div'
url_path_2 = '//*[@id="main-content"]/div/div/div[2]/div/div[4]/div[' + str(i) + ']/div'
url_path_3 = '//*[@id="main-content"]/div/div/div/div/div[5]/div[' + str(i) + ']/div'
name_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div/a/h3'
is_selected_popular_sorted = False
try:
    popular_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/input[2]')))
    #if not popular_element.is_selected():   
    popular_element.find_element_by_xpath("following-sibling::label").click()  #最も人気の料理クリック

    for a in range(9):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            more_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/div/div/div/div/button')))
            more_element.click() #さらに表示クリック

except Exception as e:
    print(e)
else:
    is_selected_popular_sorted = True
    

if not is_selected_popular_sorted:
    try:
        rearrange_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/div/div[3]/div/div/div[1]/div/div[1]/div')))
        rearrange_element.click()
        popular_element = browser.find_element_by_xpath('//*[@id="main-content"]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/label[2]')
        popular_element.click()  #最も人気の料理クリック 

        for a in range(9):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            more_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/div/div/div/div/button')))
            more_element.click() #さらに表示クリック
            

        while i < 800 :
            url_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,url_path_3)))
            URL = url_element.find_element_by_tag_name("a").get_attribute("href")
            urls.append(URL)
            ids.append(URL[-22:])
            name_element = browser.find_element_by_xpath(name_path).text
            names.append(name_element)
            name_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div/a/h3'
            i += 1
            url_path_3 = '//*[@id="main-content"]/div/div/div/div/div[5]/div[' + str(i) + ']/div'
            name_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div/a/h3'

    except Exception as f:
        print(f)

elif is_selected_popular_sorted:
    try:
        while i < 800 :
            url_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,url_path)))
            #urls.append(url_element.find_element_by_tag_name("a").get_attribute("href"))
            URL = url_element.find_element_by_tag_name("a").get_attribute("href")
            urls.append(URL)
            ids.append(URL[-22:])
            name_element = browser.find_element_by_xpath(name_path).text
            names.append(name_element)
            i += 1
            url_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div'
            name_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div/a/h3'
                      
    except NoSuchElementException:
        while i < 800 :
            url_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,url_path_2)))
            #urls.append(url_element.find_element_by_tag_name("a").get_attribute("href"))
            URL = url_element.find_element_by_tag_name("a").get_attribute("href")
            urls.append(URL)
            ids.append(URL[-22:])
            name_element = browser.find_element_by_xpath(name_path).text
            names.append(name_element)  
            i += 1
            url_path_2 = '//*[@id="main-content"]/div/div/div[2]/div/div[4]/div[' + str(i) + ']/div'     
            name_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div/a/h3'

    except Exception as e:
        print(e)

print(ids)

import pandas as pd
df = pd.DataFrame(index=[],columns=[])
df['URL'] = urls
df['NAME'] = names
df['ID'] = ids
df.to_csv("b.csv")
