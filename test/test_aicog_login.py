import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging
import sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from conftest import password, username 

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

#class AddProject():
def test_login(username, password):
    logger.info("****Started Login Test****")
   
    #old code
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    
    driver.get("https://aiwb-dev.amgen.com/")
     #driver.get("https://aiwb-test.amgen.com/")
    logger.info("****Started Login Test1****")
    Prompt_workspace_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[2]/a[2]/button')
    Prompt_workspace_button.click()
    driver.implicitly_wait(5)
    SSO_Button = driver.find_element(By.XPATH, '/html/body/uses-legacy-bootstrap/div/div/div[1]/div/div/div/div/div/button')

    SSO_Button.click()
    try:
      popup = WebDriverWait(driver, 10).until(EC.alert_is_present())
      #alert = driver.switch_to.alert
      #alert.dismiss()
      popup.dismiss()
    except Exception as e:
      logger.info("****Started Login Test00000", e)
    
    #driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    try: 
       username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input')))
    
    #username_input = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input')
       logger.info("username")
       username_input.send_keys(username)

    finally:
       logger.info("password")
    
    
    NextButton = driver.find_element(By.XPATH, '//*[@id="form20"]/div[2]/input')
    NextButton.click()
    #driver.implicitly_wait(10)
    password_input = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input')
    driver.implicitly_wait(5)
    password_input.send_keys(password)
    #driver.implicitly_wait(10)
    driver.implicitly_wait(5)
    Verify_button = driver.find_element(By.XPATH, '//*[@id="form52"]/div[2]/input')

    Verify_button.click()
    logger.info("successfully login")
    driver.implicitly_wait(30)
    #return driver
