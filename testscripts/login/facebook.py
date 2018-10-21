import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = None

def loginFB_EmptyField(driver):
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonFB = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-block btn-lg btn-fb btn-glow metro" and contains(text(),"Login with Facebook")]')))
        logging = ButtonFB.text
        status = "PASS"
        #time.sleep(5)
        ButtonFB.click()
        time.sleep(2)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            logging = driver.title
            driver.find_element_by_xpath('//input[@type="submit" and @name="login"]').click()
            try:
                alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="pam login_error_box uiBoxRed" and @id="error_box"]')))
                logging = alert.text
                status = "PASS"
                time.sleep(1)
                driver.close()
                driver.switch_to_window(window_before)
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status

def loginFB_InvalidPassword(driver, EMAIL):
    PASSWORD = "123qweasd"
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonFB = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-block btn-lg btn-fb btn-glow metro" and contains(text(),"Login with Facebook")]')))
        logging = ButtonFB.text
        #ButtonFB.click()
        status = "PASS"
        #time.sleep(5)
        ButtonFB.click()
        time.sleep(1)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            logging = driver.title
            driver.find_element_by_xpath('//input[@type="text" and @id="email"]').send_keys(EMAIL)
            driver.find_element_by_xpath('//input[@type="password" and @id="pass"]').send_keys(PASSWORD)
            driver.find_element_by_xpath('//input[@type="submit" and @name="login"]').click()
            try:
                alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="pam login_error_box uiBoxRed" and @id="error_box"]')))
                logging = alert.text
                status = "PASS"
                time.sleep(1)
                driver.close()
                driver.switch_to_window(window_before)
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status

def loginFB_Valid(driver, EMAIL, PASSWORD, SERVER):
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonFB = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-block btn-lg btn-fb btn-glow metro" and contains(text(),"Login with Facebook")]')))
        logging = ButtonFB.text
        #ButtonFB.click()
        status = "PASS"
        #time.sleep(5)
        ButtonFB.click()
        time.sleep(1)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            time.sleep(1)
            logging = driver.title
            driver.find_element_by_xpath('//input[@type="text" and @id="email"]').clear()
            time.sleep(1)
            driver.find_element_by_xpath('//input[@type="text" and @id="email"]').send_keys(EMAIL)
            time.sleep(1)
            driver.find_element_by_xpath('//input[@type="password" and @id="pass"]').send_keys(PASSWORD)
            driver.find_element_by_xpath('//input[@type="submit" and @name="login"]').click()
            time.sleep(10)
            try:
                driver.switch_to_window(window_before)
                driver.get(SERVER)
                dropdown_profile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@id="dropdown-notif" and @class="dropdown-toggle"]')))
                logging = driver.title
                status = "PASS"
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
