import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = "PASS"

def Language(driver):
    driver = driver
    try:
        modal_language = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@id="languagepopupmodal"]')))
        logging = modal_language.find_element_by_xpath('//div[@class="languagemodal-top"]').text
        time.sleep(1)
        modal_language.find_element_by_xpath('//button[contains(text(), "Bahasa Indonesia")]').click()
        time.sleep(1)
    except Exception as e:
        raise
    return driver, logging, status

def Topic(driver):
    driver = driver
    try:
        modal_topic = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@id="topicSelection"]')))
        logging = modal_topic.text
        time.sleep(1)
        modal_topic.find_element_by_xpath('//span[@class="topic-select-image"]/p[contains(text(), "Bisnis")]').click()
        modal_topic.find_element_by_xpath('//span[@class="topic-select-image"]/p[contains(text(), "Olahraga")]').click()
        modal_topic.find_element_by_xpath('//a[@class="btn btn-primary text-bold" and contains(text(), "Lanjut")]').click()
        time.sleep(3)
        status = "PASS"
    except Exception as e:
        raise
    return driver, logging, status
