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
#import os

# Configure basic logging to send INFO level and higher logs to stdout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

#class AddProject():
def test_login():
    logger.info("****Started Login Test****")
    #new code
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--incognito")
    #service = webdriver.ChromeService(executable_path="./driver/chromedriver.exe")
    #driver = webdriver.Chrome(service, Options)

    
    #old code
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options)
    #driver = webdriver.Chrome(chrome_options, desired_capabilities=DesiredCapabilities)
    driver.maximize_window()
    
    # dismiss code
    #
    #os.environ["webdriver.chrome.driver"] = chromedriver
    #driver = webdriver.Chrome(chromedriver,desired_capabilities=desired_capabilities)
    
    #driver = webdriver.Chrome("C:/Users/jverma02/AI_cg_Login/driverchromedriver.exe")
    #service = webdriver.ChromeService(executable_path="./driver/chromedriver.exe")
    #driver = webdriver.Chrome(service=service)
    driver.get("https://aiwb-dev.amgen.com/")
    logger.info("****Started Login Test1****")
    Prompt_workspace_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[2]/a[2]/button')
    Prompt_workspace_button.click()
    driver.implicitly_wait(5)

    SSO_Button = driver.find_element(By.XPATH, '/html/body/uses-legacy-bootstrap/div/div/div[1]/div/div/div/div/div/button')
    logger.info("****Started Login Test2****")
    
    SSO_Button.click()
    driver.implicitly_wait(20)
  
    
    #driver.implicitly_wait(5)
    #try:
      #WebDriverWait(driver, 2).until(EC.alert_is_present())
      #alert = driver.switch_to.alert
      #alert.dismiss()
     #except:
      #exit
    logger.info("****Started Login Test00000")
    #driver.implicitly_wait(10)
    username_input = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input')
    #username_input = driver.find_element(By.XPATH, "//*[@id='input28']")
    logger.info("username")

    username_input.send_keys("jverma02")
    logger.info("passwrd")
    #time.sleep(5)
    driver.implicitly_wait(20)
    #NextButton = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input')
    NextButton = driver.find_element(By.XPATH, '//*[@id="form20"]/div[2]/input')
    NextButton.click()
    driver.implicitly_wait(5)
    password_input = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input')
    password_input.send_keys("Vvedansh$20244")
    driver.implicitly_wait(5)
    
    logger.info("successfuly login to AI cognition")
    Verify_button = driver.find_element(By.XPATH, '//*[@id="form52"]/div[2]/input')
 
    logger.info("verified button")
    Verify_button.click()
    time.sleep(10)

    logger.info("successfully login")
    driver.implicitly_wait(30)
    time.sleep(10)