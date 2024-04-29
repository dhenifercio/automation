
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico,options=chrome_options)

navegador.get("https://www.linkedin.com/in/bruno-m-15277430/")

class Leads:
    def __init__(self, name):
      self.name = name.text
      self.position = 0
      self.company = 0
      
    def positions(self, position):
        self.position = position.text

    def companies(self, company):
        self.company = company.text

    def apresentation(self):
        print("Nome:", self.name) 
        print("Cargo:", self.position)
        print("Empresa:", self.company)    


Wait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="public_profile_contextual-sign-in"]/div/section/button'))).click()

user1 = Leads(Wait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/section[1]/div/section/section[1]/div/div[2]/div[1]/button/h1'))))
user1.positions(Wait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/section[1]/div/section/section[4]/div/ul/li[1]/div/h3/span'))))
user1.companies(Wait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/section[1]/div/section/section[4]/div/ul/li[1]/div/h4/a/span'))))
user1.apresentation()

