import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = None

def NotifPopover(driver, BUTTON):
    driver = driver
    try:
        #driver.save_screenshot("screenshot.png")
        modalnotif = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@id="onesignal-popover-dialog"]')))
        logging = modalnotif.find_element_by_xpath('//div[@class="popover-body-message"]').text + " " + BUTTON
        modalnotif.find_element_by_xpath('//button[@id="onesignal-popover-cancel-button" and contains(text(),"'+BUTTON+'")]').click()
        time.sleep(1)
        #status = "PASS"
    except Exception as e:
        driver.save_screenshot("Report/NotifPopover.png")
        logging = "Modal 'Nyalakan notifikasi' Tidak Muncul"
        #status = "FAIL"
    return driver, logging#, status

def NotifDropdown(driver):
    driver = driver
    try:
        headermenu = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@id="rootheader"]')))
        time.sleep(1)
        iconnotif = headermenu.find_element_by_xpath('//*[@id="rootheader"]/div[1]/div/div[1]/div/div/div[3]/div[2]/a/i').click()
        try:
            notif_modal = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@id="notificationmodal"]')))
            logging = notif_modal.find_element_by_xpath('//div[@class="text-center text-grey"]').text
            time.sleep(1)
            driver.find_element_by_xpath('//div[@id="notificationmodal"]').click()
            status = "PASS"
            time.sleep(1)
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status

def NotifPage(driver):
    driver = driver
    try:
        headermenu = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@id="rootheader"]')))
        time.sleep(1)
        iconnotif = headermenu.find_element_by_xpath('//*[@id="rootheader"]/div[1]/div/div[1]/div/div/div[3]/div[2]/a/i').click()
        try:
            notif_modal = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@id="notificationmodal"]')))
            logging = notif_modal.find_element_by_xpath('//div[@class="text-center text-grey"]').text
            time.sleep(1)
            notif_modal.find_element_by_xpath('//p[@class="btn text-darkgrey text-bold pull-left"]').click()
            try:
                content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div/div[2]')))
                logging = content.text
                time.sleep(1)
                status = "PASS"
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
