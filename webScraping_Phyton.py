from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import csv
import pandas as pd
import time

r=1
templist = [] 
options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome('./chromedriver', options=options)
actions = ActionChains(driver)
driver.get("https://www.linkedin.com")
botaoVaga = driver.find_element(By.XPATH, "/html/body/nav/ul/li[4]")
botaoVaga.click()
time.sleep(1)
cargos = driver.find_element(By.XPATH, "/html/body/div/header/nav/section/section[@id='jobs-search-panel']/form/section/input")
cargos.click()
cargos.send_keys("Marketing")
time.sleep(2)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()
time.sleep(2)
local = driver.find_element(By.XPATH, "/html/body/div/header/nav/section/section[@id='jobs-search-panel']/form/section[2]/input")
local.clear()
time.sleep(1)
local.send_keys("Bras")
time.sleep(2)
local.send_keys("i")
time.sleep(1)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()
time.sleep(2)
local = driver.find_element(By.XPATH, "/html/body/div/header/nav/section/section[@id='jobs-search-panel']/form/section[2]/input")
tipoDeVaga = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/form/ul/li[4]")
tipoDeVaga.click()
time.sleep(2)
opcaoDeVaga = driver.find_element(By.ID, "f_JT-0")
opcaoDeVaga.click()
time.sleep(1)
aplicarFiltro = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/form/ul/li[4]/div/div/div/button")
aplicarFiltro.click()
time.sleep(2)
aplicarNivelExp = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/form/ul/li[5]")
aplicarNivelExp.click()
time.sleep(1)
nivelExp = driver.find_element(By.ID, "f_E-0")
nivelExp.click()
time.sleep(1)
aplicarFiltro = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/form/ul/li[5]/div/div/div/button")
aplicarFiltro.click()
time.sleep(2)




import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Configurar as opções do Chrome para abrir maximizado
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

navegador = webdriver.Chrome(options=chrome_options)  # Use as opções configuradas
navegador.get("https://www.linkedin.com/home")
time.sleep(2)

botaoVaga = navegador.find_element(By.XPATH, "/html/body/nav/ul/li[4]")
botaoVaga.click()
time.sleep(1)

pesquisa = navegador.find_element(By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input")
pesquisa.send_keys("Analista de Dados")
time.sleep(2)

local = navegador.find_element(By.XPATH, "/html/body/div/header/nav/section/section[@id='jobs-search-panel']/form/section[2]/input")
local.clear()
local.send_keys("Bras")
time.sleep(2)
local.send_keys("il")
time.sleep(1)
local.send_keys(Keys.ARROW_DOWN)
local.send_keys(Keys.ENTER)
time.sleep(5)

navegador.quit()



import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By



# Configurar as opções do Chrome para abrir maximizado

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")



navegador = webdriver.Chrome(options=chrome_options)  # Use as opções configuradas

navegador.get("https://www.linkedin.com/home")

time.sleep(2)



botaoVaga = navegador.find_element(By.XPATH, "/html/body/nav/ul/li[4]")

botaoVaga.click()

time.sleep(1)



pesquisa = navegador.find_element(By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input")

pesquisa.send_keys("Analista de Dados")

time.sleep(2)



local = navegador.find_element(By.XPATH, "/html/body/div/header/nav/section/section[@id='jobs-search-panel']/form/section[2]/input")

local.clear()

local.send_keys("Bras")

time.sleep(2)

local.send_keys("il")

time.sleep(1)

local.send_keys(Keys.ARROW_DOWN)

local.send_keys(Keys.ENTER)

time.sleep(5)



navegador.quit()

