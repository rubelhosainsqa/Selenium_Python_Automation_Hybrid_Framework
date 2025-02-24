from selenium.webdriver.common.by import By
from POM.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    # For the search result product
    valid_hp_product_lct_xpath = "//div[contains(@class,'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12')]"

    # For No result text message
    no_result_test_message_lct_xpath = "//input[@id='button-search']/following-sibling::p"


    # For the search result product
    def display_status_of_hp_product(self):
        return self.check_display_status_of_element("valid_hp_product_lct_xpath",self.valid_hp_product_lct_xpath) # Used "check_display_status_of_element" method of BasePage

    # For No result text message
    def no_result_text_message(self):
        return self.retrieve_element_text("no_result_test_message_lct_xpath",self.no_result_test_message_lct_xpath) # Used "retrieve_element_text" method of BasePage
