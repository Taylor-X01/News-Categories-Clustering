import os
import sys
from turtle import clear
import pandas as pd
import time
from selenium import webdriver

Url_politics = "https://www.hespress.com/politique"
Url_business = "https://www.hespress.com/economie"
Url_curlture = "https://www.hespress.com/art-et-culture"
opts = webdriver.ChromeOptions()
opts.headless = False
driver = webdriver.Chrome(
    executable_path="C:\\chromedriver\\chromedriver100.exe")

# Choose your topic
## 1 - Politics
# Url = Url_politics
## 2 - Culture
# Url = Url_curlture
## 3 - Business
Url = Url_business

driver.get(Url)