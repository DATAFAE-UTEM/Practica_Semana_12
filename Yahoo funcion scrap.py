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
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")


def get_data(url):
    driver.get(url)
    # tiempo para interactuar con navegador
    time.sleep(8)
    # numero de filas y columnas
    rows = len(driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr"))
    cols = len(driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[2]/td"))
    print(rows)
    print(cols)
    # estructura de tabla
    data = {}
    df = pd.DataFrame(columns=['Empresa', 'Medidas de valorizacion', 'Valores'])
    # extraccion de contenido
    for r in range(1, rows + 1):
        data['Medidas de valorizacion'] = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[" + str(
                r) + "]/td[1]").text
        data['Valores'] = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[" + str(
                r) + "]/td[2]").text
        df = df.append(data, ignore_index=True)
        print(df)
        df.to_csv('Tablas data')

    # ingresar el link del listado


get_data('')

