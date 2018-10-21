import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = None

def loginGPlus_EmptyField(driver):
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonGPlus = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-block btn-lg btn-gplus btn-glow"]')))
        logging = ButtonGPlus.text
        status = "PASS"
        ButtonGPlus.click()
        time.sleep(5)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            Button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//content/span[contains(text(), "Berikutnya")]')))
            logging = driver.title
            Button.click()
            try:
                alert = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Masukkan email atau nomor telepon")]')))
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

def loginGPlus_InvalidID(driver):
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonGPlus = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-block btn-lg btn-gplus btn-glow"]')))
        logging = ButtonGPlus.text
        status = "PASS"
        ButtonGPlus.click()
        time.sleep(5)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            Button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//content/span[contains(text(), "Berikutnya")]')))
            driver.find_element_by_xpath('//input[@id="identifierId" and @type="email"]').send_keys('vd234sf234-/!.,>')
            logging = driver.title
            Button.click()
            try:
                alert = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Masukkan email atau nomor telepon yang valid")]')))
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

def loginGPlus_InvalidPass(driver, ID):
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonGPlus = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-block btn-lg btn-gplus btn-glow"]')))
        logging = ButtonGPlus.text
        status = "PASS"
        ButtonGPlus.click()
        time.sleep(5)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            Button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//content/span[contains(text(), "Berikutnya")]')))
            driver.find_element_by_xpath('//input[@id="identifierId" and @type="email"]').clear()
            driver.find_element_by_xpath('//input[@id="identifierId" and @type="email"]').send_keys(ID)
            time.sleep(1)
            logging = driver.title
            Button.click()
            time.sleep(1)
            try:
                PassField = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
                time.sleep(1)
                PassField.send_keys("123123123")
                time.sleep(1)
                driver.find_element_by_xpath('//content/span[contains(text(), "Berikutnya")]').click()
                try:
                    alert = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Sandi salah. Coba lagi atau klik Lupa sandi untuk menyetel ulang.")]')))
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
    except Exception as e:
        raise
    return driver, logging, status

def loginGPlus_Valid(driver, ID, PASSWORD):
    driver = driver
    try:
        window_before = driver.window_handles[0]
        ButtonGPlus = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-block btn-lg btn-gplus btn-glow"]')))
        logging = ButtonGPlus.text
        status = "PASS"
        ButtonGPlus.click()
        time.sleep(5)
        try:
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            Button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//content/span[contains(text(), "Berikutnya")]')))
            driver.find_element_by_xpath('//input[@id="identifierId" and @type="email"]').clear()
            driver.find_element_by_xpath('//input[@id="identifierId" and @type="email"]').send_keys(ID)
            logging = driver.title
            Button.click()
            time.sleep(1)
            try:
                PassField = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
                time.sleep(1)
                PassField.send_keys(PASSWORD)
                time.sleep(1)
                driver.find_element_by_xpath('//content/span[contains(text(), "Berikutnya")]').click()
                time.sleep(1)
                try:
                    AllowButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//content/span[contains(text(), "Izinkan")]')))
                    logging = AllowButton.text
                    AllowButton.click()
                    time.sleep(5)
                    driver.switch_to_window(window_before)
                    logging = driver.title
                except Exception as e:
                    try:
                        AllowButton = driver.find_element_by_xpath('//content/span[contains(text(), "Allow")]')
                        logging = AllowButton.text
                        AllowButton.click()
                        time.sleep(5)
                        driver.switch_to_window(window_before)
                        logging = driver.title
                    except Exception as e:
                        status = "PASS"
                        driver.switch_to_window(window_before)
                        time.sleep(5)
                        logging = driver.title
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
