from selenium.webdriver.common.by import By
from POM.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    # For the change your password text
    change_your_password_lct_link_text = "Change your password"

    # For the change your password text
    def retrieve_the_text_of_change_your_password(self):
        return self.check_display_status_of_element("change_your_password_lct_link_text",self.change_your_password_lct_link_text) # Used "check_display_status_of_element" method of BasePage

