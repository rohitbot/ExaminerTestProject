from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Pages.TradeRequestPageObjects import TradeRequestPage
import time


class AddTradeRequest:

    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def add_trade_request_actions(self, driver):
        trade_request_page = TradeRequestPage(driver)
        employee_lookup_icon = trade_request_page.employee_lookup_icon_id
        delay = 10
        self.driver.find_element_by_id(trade_request_page.trade_request_add_button_id).click()
        try:
            WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, employee_lookup_icon)))
            print("Page is ready!")
            driver.find_element_by_id('ibtnEmployeeLookup').click()
        except TimeoutException:
            print("Loading took too much time!")
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, trade_request_page.employee_code_id)))
        self.driver.find_element_by_id(trade_request_page.employee_code_id).send_keys('DONTO')
        self.driver.find_element_by_id(trade_request_page.lookup_button_id).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(trade_request_page.employee_code_link_text).click()
        time.sleep(2)
        self.driver.find_element_by_id(trade_request_page.trade_request_brokerage_account_lookup_button).click()
        self.driver.find_element_by_id(trade_request_page.brokerage_account_number_lookup_page_id).send_keys('171001 '
                                                                                                             'TEST '
                                                                                                             'ACCOUNT')
        self.driver.find_element_by_id(trade_request_page.brokerage_account_lookup_result_id).click()
        self.driver.find_element_by_id(trade_request_page.trade_request_adv_lookup).click()
        adv_lookup_frame = self.driver.find_element_by_name(trade_request_page.adv_security_lookup_frame_name)
        driver.switch_to.frame(adv_lookup_frame)
        try:
            elem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'txtSymbol')))
            print('Element Visible')
            driver.find_element_by_id('txtSymbol').send_keys('ATW')
            driver.find_element_by_id('btnLookup').click()
            #time.sleep(10)
            WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'securityDetailGrid_ctl00__0')))
            driver.find_element_by_id('securityDetailGrid_ctl00__0').click()
        except TimeoutException:
            print('Element not found')
        driver.switch_to.default_content()
        if driver.find_element_by_id('CmbTransType_RadCmbTransactionType_Arrow').is_displayed() == 1:
            print('Frame in place')
        else:
            print('Frame out of place')
        driver.find_element_by_id('CmbTransType_RadCmbTransactionType_Arrow').click()
        select_buy = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#CmbTransType_RadCmbTransactionType_i2_lblTranTypeCodeVal')))
        select_buy.click()
        try:
            myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'txtRequestQuantity')))
            print("Page is ready now!")
            driver.find_element_by_id('txtRequestQuantity').click()
        except TimeoutException:
            print("Loading took too much time!")
        driver.find_element_by_id('txtRequestQuantity').send_keys('100')
        try:
            myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'txtRequestPrice')))
            print("Page is ready now!")
            driver.find_element_by_id('txtRequestPrice').click()
        except TimeoutException:
            print("Loading took too much time!")
        driver.find_element_by_id('txtRequestPrice').send_keys('100')
        driver.find_element_by_id('btnSave').click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        print('Step4')
        print('Check if this got through')
        #self.driver.find_element_by_id(trade_request_page.trade_request_security_type_id)










