from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time as driver
import pandas as pd 
import re

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver_path = 'C:\\Users\\hyde\\OneDrive\\Escritorio\\proyecto_django_rest\\Practicando_selenium\\chromedriver.exe'
driver = webdriver.Chrome(driver_path,chrome_options=options)

#inicializar navegador

driver.get('https://digimoncard.io/top/')

cards = driver.find_element_by_id('restricted-cards').text
cards2 = cards.split('\n')

name = list()
decks = list()

for i in range(0,len(cards2),2):
    name.append(cards2[i])
    decks.append(cards2[i +1])

    
df = pd.DataFrame()
df['Name Card'] = name
df['Deck Card'] = decks

print(df)
    































''' 
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')))).click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#term'))).send_keys("Madrid")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a/span[2]'))).click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/main/div[4]/div/section[5]/section/div/article/section[1]/ul/li[2]/h2/a'))).click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul/li[1]/ul')))

data_columnas = driver.find_element_by_xpath('/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul')
data =  data_columnas.text
data_filtrada = data.split('Mañana')[0].split('\n')[1:-1]
print(data) '''