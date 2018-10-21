import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = None

def LoginRegister(driver):
    driver = driver
    try:
        headerleft = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav navbar-icon navbar-right"]')))
        SignIn = headerleft.find_element_by_xpath('//a[@class="btn btn-link color-primary" and @href="/login"]')
        logging = SignIn.text
        SignIn.click()
        status = "PASS"
    except Exception as e:
        raise
    return driver, logging, status
