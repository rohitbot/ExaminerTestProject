from _ast import Assert

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

from selenium.webdriver.remote.webelement import WebElement


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\rohit.behera\PycharmProjects\Examiner\Test\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Browser instantiated")

    def testloginvalid(self):
        driver = self.driver
        driver.get("http://examiner-web.southcentralus.cloudapp.azure.com/Examiner/WebApps/LoginHome/Login.aspx")
        login = LoginPage(driver)
        login.enter_username('Donto')
        login.enter_password('jmon@16')
        login.click_login()
        homepage = HomePage(driver)
        homepage.confirm_login()
        homepage.confirm_logout_tab()
        time.sleep(3)
        print('Login complete')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Login Complete')
