from selenium import webdriver


class TradeInfoDropdown:
    from selenium.webdriver import ActionChains
    from Pages.TradeRequestPageObjects import TradeRequestPage

    def __init__(self, driver):
        self.driver = driver
        self.tradeinfo_tab_xpath = '//*[@id="ctrlHeader_ExaminerMenu_radExaminerMenu"]/ul/li[2]/a/span'
        self.traderequest_tab_xpath = '//*[@id="ctrlHeader_ExaminerMenu_radExaminerMenu"]/ul/li[2]/div/ul/li[1]/a'
        self.confirmdetails_tab_xpath = '//*[@id="ctrlHeader_ExaminerMenu_radExaminerMenu"]/ul/li[2]/div/ul/li[2]/a'
        self.accounttrades_tab_xpath = '//*[@id="ctrlHeader_ExaminerMenu_radExaminerMenu"]/ul/li[2]/div/ul/li[3]/a'
        self.orders_tab_xpath = '//*[@id="ctrlHeader_ExaminerMenu_radExaminerMenu"]/ul/li[2]/div/ul/li[4]/a'

    def select_trade_info_tab(self, driver):
        self.driver = driver
        trade_info = self.driver.find_element_by_xpath(self.tradeinfo_tab_xpath)
        hover = self.ActionChains(driver).move_to_element(trade_info)
        hover.perform()

    def select_trade_request_tab(self):
        self.driver.find_element_by_xpath(self.traderequest_tab_xpath).click()




