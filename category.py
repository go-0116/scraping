from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path='/home/gm116/bin/chromedriver',options=chrome_options)
url = 'https://www.ubereats.com/jp/feed?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVCOCU4QiVFOCVCMCVCNyVFNSU4QyVCQSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUowUWd4NjdLTUdHQVJkMlpiT2JMWkhQRSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS42NjE5NzA3JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjcwMzc5NSU3RA%3D%3D'
browser.get(url)

url2 = 'https://www.ubereats.com/search?q=Burger'
browser.get(url2)

url_element = browser.find_element_by_xpath('//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[1]/div')
print(url_element)
## //*[@id="main-content"]/div/div/div[2]/div/div[2]/div[1]/div/a