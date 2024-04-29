from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver import Chrome 

web_driver_manager = ChromeDriverManager()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(web_driver_manager.install())
driver = Chrome(service=service, options=chrome_options)

driver.get("https://www.instagram.com/")
driver.maximize_window()