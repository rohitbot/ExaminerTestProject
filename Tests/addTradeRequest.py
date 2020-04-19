from selenium import webdriver
import unittest

from Actions.TradeInfoDropdown import TradeInfoDropdown
from Pages.loginPage import LoginPage
from Actions.AddTradeRequest import AddTradeRequest


class VerifyTradeRequestPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\rohit.behera\PycharmProjects\Examiner\Test\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Browser instantiated")

    def testAddTradeRequestPage(self):
        driver = self.driver
        driver.get("http://examiner-web.southcentralus.cloudapp.azure.com/Examiner/WebApps/LoginHome/Login.aspx")
        login = LoginPage(driver)
        login.enter_username('Donto')
        login.enter_password('jmon@16')
        login.click_login()
        validate = TradeInfoDropdown(driver)
        validate.select_trade_info_tab(driver)
        validate.select_trade_request_tab()
        add_trade = AddTradeRequest(driver)
        add_trade.add_trade_request_actions(driver)



    @classmethod
    def tearDownClass(cls):
       cls.driver.close()
       cls.driver.quit()
       print('Login Complete')