

class TradeRequestPage:
    def __init__(self, driver):
        self.driver = driver
        self.trade_request_add_button_id = 'btnAdd'
        self.trade_request_filter_button_id = 'btnFilter'
        self.trade_request_disable_page_refresh_id = 'radDisablePageRefresh'
        self.trade_request_enable_page_refresh_id = 'radEnablePageRefresh'
        self.trade_request_employee_id = 'radEmployeeAutoSuggest_radAutoEmployee_Input'
        self.trade_request_brokerage_account_id = 'txtBrokerageAccount'
        self.trade_request_security_type_id = 'ctlSecurityAutoSuggest_radcmbST_exRadCombo_Input'
        self.trade_request_adv_lookup = 'ctlSecurityAutoSuggest_btnAdvLookup'
        self.employee_lookup_icon_id = 'ibtnEmployeeLookup'
        self.employee_code_id = 'txtEmployeeCode'
        self.lookup_button_id = 'btnLookup'
        self.employee_code_link_text = 'DONTO'
        self.trade_request_brokerage_account_lookup_button = 'ibtnBrokerageAccountLookup'
        self.brokerage_account_number_lookup_page_id = 'txtBrokerageAccountNumber'
        self.adv_security_lookup_frame_name = 'SecurityDialog_ctlSecurityAutoSuggest'
        self.brokerage_account_lookup_result_id = 'radGrdBA_ctl00_ctl04_lnkBACD'



