import boto3


dynamodb = boto3.resource("dynamodb", region_name='ap-northeast-1')
list(dynamodb.tables.all())

#table = dynamodb.Table('Daily_Scraping')
table = dynamodb.create_table(
TableName = 'Daily_scraping',
    KeySchema = [
        {
            'AttributeName' : 'ID',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'location',
            'KeyType' : 'RANGE'
        }
    ],
    AttributeDefinitions =[
        {
            'AttributeName' : 'id',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'location',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'cateory',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'url',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'rank',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'date',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'restaurant_name',
            'AttributeType' : 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits':1,
        'WriteCapacityUnits':1
    }
)


'''
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

for Location in location_list:
    
    try:
        browser.get(url)
        change_element = browser.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/a')
        change_element.click() #配送先クリック//*[@id="wrapper"]/div[5]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/a
    except NoSuchElementException:
        change_element_1 = browser.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/a')
        change_element_1.click() 
    
    sleep(1)
    location_element = browser.find_element_by_xpath('//*[@id="location-typeahead-location-manager-input"]')
    location_element.send_keys(Location)     #//*[@id="location-typeahead-location-manager-input"]
    sleep(1)
    location_element.send_keys(Keys.ENTER)
    sleep(1)
    table.put_item(
        Item= {
            'location' : Location,
            'url':browser.current_url
        }
    )
'''





