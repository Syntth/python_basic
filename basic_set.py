##IMPORTANDO VARIOS MODULOS Y LIBRERIAS
### import modules/libraries
##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##from selenium.common.exceptions import TimeoutException
##from selenium.webdriver.common.by import By
###import selenium.webdriver.support.expected_conditions import EC
##import selenium.webdriver.support.ui as ui
##import os
##import time
##
##options = webdriver.ChromeOptions()
##options.add_argument('--ignore-certificate-erros')
##options.add_argument('--ignore-ssl-errors')
##dir_path = os.path.dirname(os.path.realpath(__file__))
##chromedriver = dir_path + "/chromedriver"
##os.environ["webdriver.chrome.driver"] = chromedriver
##driver = webdriver.Chrome(options=options, executable_path= chromedriver)
##driver.get("http://www.facebook.com")
##time.sleep(5) #miliseconds
##driver.close()


##FORMA BÁSICA
## import modules/libraries
from selenium import webdriver
import os
import time

##driver path setup
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
driver = webdriver.Chrome(executable_path= chromedriver)
time.sleep(5) #miliseconds
driver.close()