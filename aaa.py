from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_options = Options ()
chrome_options.add_experimental_option("detach",True)
servico =Service(ChromeDriverManager().install())

navegador =webdriver.Chrome(service=servico,options=chrome_options)
navegador.get("https://siga.cps.sp.gov.br/aluno/login.aspx")
navegador.find_element("xpath",'//*[@id="vSIS_USUARIOID"]').send_keys(50908798857)
navegador.find_element("xpath",'//*[@id="vSIS_USUARIOSENHA"]').send_keys('190605DL')
navegador.find_element("xpath",'//*[@id="TABLE2"]/tbody/tr[5]/td[2]/input').click()
navegador.find_element("xpath",'//*[@id="ygtvlabelel6Span"]').click()


