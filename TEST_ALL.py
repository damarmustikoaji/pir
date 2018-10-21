import sys
import unittest
import time
from selenium import webdriver
from HTMLTestRunner_report import HTMLTestRunner

from testscripts.browser.browser import DriverBrowser
from testscripts.notifikasi.notifikasi import NotifPopover
from testscripts.login.login import LoginRegister
from testscripts.logout.logout import Logout
from testscripts.login.facebook import loginFB_InvalidPassword
from testscripts.login.facebook import loginFB_Valid
from testscripts.login.google import loginGPlus_InvalidID
from testscripts.login.google import loginGPlus_Valid
from testscripts.news.news import News
from testscripts.news.news import NewsInvalidURL
from testscripts.news.comment import CommentNoLogin
from testscripts.news.comment import Comment

import random
from random import randint

SERVER = None
EMAIL = None
PASSWORD = None
BROWSER = None

class Test1_Login(unittest.TestCase):#hapus unittest.TestCase to skip
    "Test Case Login"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)
        #self.driver.set_page_load_timeout(60)
        #self.driver.implicitly_wait(10)

    def test_Login_001(self):
        "Kumparan Login with Facebook - Invalid Password"
        self.driver.get(SERVER+"login")
        driver, logging = NotifPopover(self.driver, "TIDAK")
        self.startTime = time.time()
        #driver, logging, status = LoginRegister(self.driver)
        driver, logging, status = loginFB_InvalidPassword(self.driver, "damar.facebook@yahoo.com")
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_Login_002(self):
        "Kumparan Login with Google - Valid data"
        self.driver.get(SERVER+"login")
        #driver, logging = NotifPopover(self.driver, "TIDAK")
        self.startTime = time.time()
        #driver, logging, status = LoginRegister(self.driver)
        driver, logging, status = loginGPlus_Valid(self.driver, "damarresin", "orangsukses")
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

class Test2_News(unittest.TestCase):
    "Test Case News"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)
        #self.driver.set_page_load_timeout(60)
        #self.driver.implicitly_wait(10)

    def test_News_001(self):
        "Kumparan Users see news - Valid URL"
        self.driver.get(SERVER)
        driver, logging = NotifPopover(self.driver, "TIDAK")
        self.startTime = time.time()
        #driver, logging, status = LoginRegister(self.driver)
        driver, logging, status = News(self.driver)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_News_002(self):
        "Kumparan Users see news - Invalid URL"
        #self.driver.get(SERVER)
        #driver, logging = NotifPopover(self.driver, "TIDAK")
        self.startTime = time.time()
        #driver, logging, status = LoginRegister(self.driver)
        driver, logging, status = NewsInvalidURL(self.driver)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

class Test3_Comment(unittest.TestCase):
    "Test Case Comment"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)
        #self.driver.set_page_load_timeout(60)
        #self.driver.implicitly_wait(10)

    def test_Comment_001(self):
        "Kumparan Users Comment - Not Log In"
        self.driver.get(SERVER)
        driver, logging = NotifPopover(self.driver, "TIDAK")
        self.startTime = time.time()
        #driver, logging, status = LoginRegister(self.driver)
        driver, logging, status = News(self.driver)
        driver, logging, status = CommentNoLogin(self.driver)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_Comment_002(self):
        "Kumparan Users Comment - Valid"
        #self.driver.get(SERVER+"login")
        #driver, logging = NotifPopover(self.driver, "TIDAK")
        self.startTime = time.time()
        #driver, logging, status = LoginRegister(self.driver)
        driver, logging, status = loginGPlus_Valid(self.driver, "damarresin", "orangsukses")
        #driver, logging, status = News(self.driver)
        driver, logging, status = Comment(self.driver, "News menarik")
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

if __name__ == '__main__':
    command = len(sys.argv)
    if command == 3:#5
        BROWSER = sys.argv.pop()
        SERVER = sys.argv.pop()
        if "http" not in SERVER:
            SERVER = "http://"+SERVER
        #PASSWORD = sys.argv.pop()
        #EMAIL = sys.argv.pop()
    else:
        sys.exit("ERROR : Please check again your argument (python test.py url browser > report)")
    HTMLTestRunner.main()
    #unittest.main()
