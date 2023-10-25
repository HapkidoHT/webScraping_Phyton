Tutorial de como executar o arquivo.py pelo cmd.

clicar no link abaixo:
https://pt.wikihow.com/Executar-o-Arquivo-Python-no-Prompt-de-Comando-no-Windows

import pandas as pd
from selenium import webdriver

# Configurar as opções do Chrome (pode adicionar mais opções, se necessário)
chrome_options = webdriver.ChromeOptions()

# Especificar o caminho completo para o ChromeDriver
path = ('./chromedriver.exe')

# URL que você deseja acessar
url = 'https://velsis.qualyteam.com.br/login/login.aspx'

# Inicializar o driver do Chrome com as opções e o caminho
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
driver.get(url)
