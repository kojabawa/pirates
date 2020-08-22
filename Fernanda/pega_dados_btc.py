
#importando módulos
import pandas as pd
from selenium import webdriver
import time
import re
import os
import shutil
import schedule

def pega_dados_btc():
    
    #definindo driver
    driver = webdriver.Chrome('chromedriver.exe')
    
    # escolhendo url para acessar
    url ="https://www.cryptodatadownload.com/data/coinbase/"
    
    #espera antes de morrer caso tente fazer algo
    driver.implicitly_wait(10)

    #acessando o url pelo driver
    driver.get(url)

    #espera 10 segundos
    time.sleep(10)

    #scrollar
    driver.execute_script("window.scrollTo(0, 600)") 

    #  clicando no botão com os dados do bitcoin
    driver.find_element_by_link_text("""[Daily]""").click()

    #espera 5 segundos
    time.sleep(5)

    # fechando o driver
    driver.close()

    # movimentando de uma pasta para outra (ATENÇÃO: AlTERAR OS VALORES CONFORME SUAS PASTAS)
    source = r'C:\Users\ferna\Downloads'
    dest = r'C:\Users\ferna\OneDrive - Fundacao Getulio Vargas - FGV\2020.2\Desafio cripto\Extrai Dados'
    files = os.listdir(source) #listando arquivos no diretório
    for f in files:
        if 'Coinbase' in f:
            shutil.move(source + "\\" + f,dest)


schedule.every().day.at("23:00").do(pega_dados_btc)

while True:
    schedule.run_pending()
    time.sleep(1)

