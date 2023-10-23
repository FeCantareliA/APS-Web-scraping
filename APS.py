from time import sleep 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
servico=Service()
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
navegador=webdriver.Chrome(service=servico,options=options)
url='https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx'
navegador.get(url)
acesso=navegador.find_element(By.XPATH, '/html/body/form/div[4]/div/div[4]/div[3]/a')
acesso.click()
acesso.clear
sleep(3)
for i in range(20,21):
    acesso = navegador.find_element(By.ID,f'cphBody_lkAno{i}')
    acesso.click()
    for i in range(1,13):
        sleep(3)
        acesso = navegador.find_element(By.ID,f'cphBody_lkMes{i}')
        acesso.click()
        sleep(3)
        acesso = navegador.find_element(By.ID,f'cphBody_ExportarBOLink')
        acesso.click()
    




