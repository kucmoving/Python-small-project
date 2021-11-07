import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import numpy as np
import pandas as pd
#------------------------------------------set the time ----------------------------------------------------#
# end date should be today, and the format should be YYYY-MM--DD
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
yesterday = int(now.day) - 1
raw_yesterday = datetime.datetime(year,month,yesterday)
real_yesterday = raw_yesterday.strftime('%Y-%m-%d')

#------------------------------------------setup selenium------------------------------------------------------#
options = webdriver.ChromeOptions()
#options.add_argument('headless')
browser = webdriver.Chrome("C:/Users/carro/Desktop/chromedriver.exe", options=options)

#------------------------------------------bs4 in selenium browser----------------------------------------------#
browser.get("https://ycharts.com/indicators/us_investor_sentiment_bullish")
soup = BeautifulSoup(browser.page_source, "html.parser")                            #CTRL + U to check where you want to makesoup
bull_num = soup.find_all("td", class_= "col-6")[13].text.strip()                    #to clear the text with .text.strip()
print(bull_num)
browser.get("https://ycharts.com/indicators/us_investor_sentiment_bearish")
soup = BeautifulSoup(browser.page_source, "html.parser")
bear_num = soup.find_all("td", class_= "col-6")[13].text.strip()
print(bear_num)

#-----------------------------------------to store it in csv-------------------------------------------------#
message = str(f"{real_yesterday},{bull_num}, {bear_num}") #### make it in to string and input in csv
with open("storage.csv", "w") as file:
    message = message.split()
    for _ in message:
        file.write(_)

file = "storage.csv"
df = pd.read_csv(file)   #只讀取2行

