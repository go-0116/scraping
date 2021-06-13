from logging import exception
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(executable_path='/home/gm116/bin/chromedriver',options=chrome_options)
url = 'https://www.ubereats.com/jp/feed?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVCOCU4QiVFOCVCMCVCNyVFNSU4QyVCQSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUowUWd4NjdLTUdHQVJkMlpiT2JMWkhQRSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS42NjE5NzA3JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjcwMzc5NSU3RA%3D%3D'
browser.get(url)
browser.implicitly_wait(10)

urls = []
i = 1
url_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div'
url_path_2 = '//*[@id="main-content"]/div/div/div[2]/div/div[4]/div[' + str(i) + ']/div'
url_path_3 = '//*[@id="main-content"]/div/div/div/div/div[5]/div[' + str(i) + ']/div'

try :
    popular_element = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/input[2]')
    if not popular_element.is_selected():
        popular_element.find_element_by_xpath("following-sibling::label").click()  #最も人気の料理クリック
    
    
    for a in range(9):
        more_element = browser.find_element_by_xpath('//*[@id="main-content"]/div/div/div[2]/div/button')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        more_element.click()  #さらに表示クリック
        sleep(4)

    try:

        while i < 5 :
            url_element = browser.find_element_by_xpath(url_path)
            urls.append(url_element.find_element_by_tag_name("a").get_attribute("href"))
            i += 1
            url_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[' + str(i) + ']/div'

    except NoSuchElementException:

        while i < 5 :
            url_element = browser.find_element_by_xpath(url_path_2)
            urls.append(url_element.find_element_by_tag_name("a").get_attribute("href"))
            i += 1
            url_path_2 = '//*[@id="main-content"]/div/div/div[2]/div/div[4]/div[' + str(i) + ']/div'        

except NoSuchElementException :
    rearrange_element = browser.find_element_by_xpath('//*[@id="main-content"]/div/div[3]/div/div/div[1]/div/div[1]/div')
    rearrange_element.click()
    popular_element = browser.find_element_by_xpath('//*[@id="main-content"]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/label[2]')
    popular_element.click()  #最も人気の料理クリック

    for a in range(9):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        more_element = browser.find_element_by_xpath('//*[@id="main-content"]/div/div/div/div/button')
        more_element.click() #さらに表示クリック
        sleep(4)

    while i < 5 :
        url_element = browser.find_element_by_xpath(url_path_3)
        urls.append(url_element.find_element_by_tag_name("a").get_attribute("href"))
        i += 1
        url_path_3 = '//*[@id="main-content"]/div/div/div/div/div[5]/div[' + str(i) + ']/div'

print(urls)
