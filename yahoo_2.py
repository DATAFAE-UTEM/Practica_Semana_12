#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importaciones
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Users\\Admin\\Desktop\\python\\driver\\chromedriver.exe")

url = 'https://es.finance.yahoo.com/quote/COPEC.SN/key-statistics?p=COPEC.SN'

# Información asociada a la tabla
driver.get(url)
print(driver.title)
time.sleep(8)

rows = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[2]/td"))
print(rows) # 9
print(cols) # 2

print("Medidas_de_valorizacion"+";"+"Valor")

for r in range(1,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end=";")
    print()