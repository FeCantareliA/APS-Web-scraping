import pandas as pd
from time import sleep 
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import shutil
salvar= "C:\\Users\\Felipe\\OneDrive\\Área de Trabalho\\Visual Studio\\Projetos\\APS 2\\arquivos"
servico=Service()
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_experimental_option("prefs", {"download.default_directory": salvar})
navegador=webdriver.Chrome(service=servico,options=option)
url='https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx'
navegador.get(url)
acesso=navegador.find_element(By.XPATH, '/html/body/form/div[4]/div/div[4]/div[3]/a')
acesso.click()
acesso.clear
sleep(3)
for i in range(20,23):
    salvar= "C:\\Users\\Felipe\\OneDrive\\Área de Trabalho\\Visual Studio\\Projetos\\APS 2\\arquivos"
    acesso = navegador.find_element(By.ID,f'cphBody_lkAno{i}')
    acesso.click()
    for i in range(1,13):
        sleep(3)
        acesso = navegador.find_element(By.ID,f'cphBody_lkMes{i}')
        acesso.click()
        sleep(3)
        acesso = navegador.find_element(By.ID,f'cphBody_ExportarBOLink')
        acesso.click()
for i in range(20,23):
    for j in range(1,13):
        for f in os.listdir(salvar):
            filename = salvar + "\\" + f 
            if filename==f'C:\\Users\\Felipe\\OneDrive\\Área de Trabalho\\Visual Studio\\Projetos\\APS 2\\arquivos\\DadosBO_20{i}_{j}(FURTO DE VEÍCULOS).xls':
                shutil.move(filename,os.path.join(salvar,r"DadosBO_20{}_{}(FURTO DE VEÍCULOS).csv".format(i,j)))