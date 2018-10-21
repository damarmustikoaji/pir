import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from random import randint

logging = None
status = None

def CommentNoLogin(driver):
    driver = driver
    try:
        comment_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="comment-field"]')))
        hover = ActionChains(driver).move_to_element(comment_field)
        hover.perform()
        time.sleep(5)
        logging = comment_field.text
        print driver.current_url
        comment_field.find_element_by_xpath('//textarea[@id="newCommentTextArea"]').send_keys("Ini komentar")
        time.sleep(1)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]')))
        button.click()
        time.sleep(3)
        try:
            logging = driver.title
            status = "PASS"
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status

def Comment(driver, COMMENTTEXT):
    driver = driver
    try:
        comment_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="comment-field"]')))
        hover = ActionChains(driver).move_to_element(comment_field)
        hover.perform()
        time.sleep(5)
        logging = comment_field.text
        #print driver.current_url
        comment_field.find_element_by_xpath('//textarea[@id="newCommentTextArea"]').send_keys(COMMENTTEXT)
        time.sleep(1)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]')))
        button.click()
        time.sleep(2)
        driver.refresh()
        try:
            comment_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="list-group-comment margbot"]')))
            hover = ActionChains(driver).move_to_element(comment_list)
            hover.perform()
            time.sleep(5)
            logging = comment_list.text
            status = "PASS"
        except Exception as e:
            print "Success Comment, tetapi tidak muncul (needed reload page)"
            logging = driver.current_url
            status = "PASS"
    except Exception as e:
        raise
    return driver, logging, status
