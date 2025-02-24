from selenium.webdriver.common.by import By
from POM.AccountPage import AccountPage
from POM.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    # For the email address field
    email_address_field_lct_name = "email"
    # For the password field
    password_field_lct_name = "password"
    # For the login button
    login_button_lct_xpath = "//input[@value='Login']"
    # For the waring message when inputting invalid credentials
    warning_message_lct_xpath = "//div[@class='alert alert-danger alert-dismissible']"



    # For the email address field
    def enter_email_address(self,email_address_text):
        self.type_into_element(email_address_text,"email_address_field_lct_name",self.email_address_field_lct_name) # Used "type_into_element" method of BasePage

    # For the password field
    def enter_password(self, password_text):
        self.type_into_element(password_text,"password_field_lct_name",self.password_field_lct_name) # Used "type_into_element" method of BasePage

    # For the login button
    def click_on_the_login_button(self):
        self.element_click("login_button_lct_xpath",self.login_button_lct_xpath) # Used "element_click" method of BasePage
        return AccountPage(self.driver) #Return the POM>>AccountPage.py file as an object

    # This method is merged 3 method (enter_email_address+enter_password+click_on_the_login_button) to one method
    def login_to_application(self,email_address_text,password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_on_the_login_button()

    # For the waring message when inputting invalid credentials
    def retrieve_waring_message(self):
        return self.retrieve_element_text("warning_message_lct_xpath",self.warning_message_lct_xpath) # Used "retrieve_element_text" method of BasePage
