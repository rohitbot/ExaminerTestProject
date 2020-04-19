class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.home_tab_xpath = '//*[@id="ctrlHeader_ExaminerMenu_radExaminerMenu"]/ul/li[1]/a/span'
        self.logout_tab_xpath = '//*[@id="ctrlHeader_DropDownNav_radiTradeMenu"]/ul/li[2]/div/ul/li[2]/a/span'

    def confirm_login(self):
        self.driver.find_element_by_xpath(self.home_tab_xpath).clear
        self.driver.find_element_by_xpath(self.home_tab_xpath).is_displayed()

    def confirm_logout_tab(self):
        self.driver.find_element_by_xpath(self.logout_tab_xpath).clear
        self.driver.find_element_by_xpath(self.logout_tab_xpath).is_displayed()