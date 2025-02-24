from selenium.webdriver.common.by import By
from POM.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    # For the successfully message
    successfully_account_creation_message_filed_lct_xpath = "//div[@id='content']/h1"


    # For the successfully message
    def retrieve_successfully_account_creation_message(self):
        return self.retrieve_element_text("successfully_account_creation_message_filed_lct_xpath",self.successfully_account_creation_message_filed_lct_xpath) # Used "retrieve_element_text" method of BasePage
