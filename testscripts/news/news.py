import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from random import randint

logging = None
status = None

def News(driver):
    driver = driver
    try:
        content = driver.find_elements_by_xpath('//div[@class="panel-body card-content"]/a[@class="btn-block"]/h4')
        count = len(content)
        count = count - 1
        pilih = randint(0, count)
        no = 0
        for baca in content:
            if no == pilih:
                hover = ActionChains(driver).move_to_element(baca)
                hover.perform()
                time.sleep(2)
                logging = baca.text
                baca.click()#find_element_by_xpath('//a[@class="btn-block"]/h4').click()
                try:
                    postingan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="panel card no-border"]')))
                    print driver.current_url
                    logging = postingan.text
                    status = "PASS"
                    time.sleep(5)
                except Exception as e:
                    raise
                break
            no=no+1
    except Exception as e:
        raise
    return driver, logging, status

def NewsInvalidURL(driver):
    driver = driver
    try:
        #postingan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="panel card no-border"]')))
        driver.get(driver.current_url+"123x")
        try:
            postingan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="panel card no-border"]/div/h4[contains(text(), "Story tidak ditemukan")]')))
            print driver.current_url
            logging = postingan.text
            status = "PASS"
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status

def Read(driver):
    driver = driver
    try:
        postingan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="panel card no-border"]')))
        print driver.current_url
        logging = postingan.text
        if "tidak ditemukan" in logging:
            status = "FAIL"
        else:
            status = "PASS"
            time.sleep(5)
    except Exception as e:
        raise
    return driver, logging, status
