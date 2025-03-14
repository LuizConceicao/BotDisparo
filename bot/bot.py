from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pd import contatosDf
import urllib

# Selenium não fala ao navegador que ele está sendo controlado
SilencioSelenium = Options()
SilencioSelenium.add_experimental_option("excludeSwitches", ["enable-automation"])
SilencioSelenium.add_experimental_option("useAutomationExtension", False)

# Caminho do seu perfil no Chrome
caminhoPerfil = r"C:\Users\luizc\AppData\Local\Google\Chrome\User Data"

SilencioSelenium.add_argument(f"--user-data-dir={caminhoPerfil}")
SilencioSelenium.add_argument("--profile-directory=Default")

navegador = webdriver.Chrome(options=SilencioSelenium)
navegador.get("https://www.google.com")
navegador.get("https://web.whatsapp.com/")

# Espera aparecer o elemento que tem como ID de "side"
while len(navegador.find_elements(By.ID, "side")) < 1:
    sleep (3)
    
# Já estamos com o login feito no Whatsapp web
for i, mensagem in enumerate (contatosDf["Mensagem"]):
    pessoa = contatosDf.loc [i, "Nome"]
    numero = contatosDf.loc [i, "Numero"]
    texto = urllib.parse.quote(f"Oi, {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        sleep (3)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)
    sleep (5)

       

