from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from POM.LoginPage import LoginPage
from POM.RegisterPage import RegisterPage
from POM.SearchPage import SearchPage


class HomePage(BasePage): # HomePage is a child class of BasePage class
    def __init__(self,driver): # The child class is used constructor of Super/parent BasePage class
        super().__init__(driver)

    # For the search field
    search_box_field_lct_name = "search" #lct == Location
    # For the search icon
    search_button_lct_xpath = "//button[contains(@class,'btn btn-default btn-lg')]"
    # For the My Account button
    my_account_button_lct_xpath = "//span[text()='My Account']"
    # For the Login button
    login_button_lct_link_text = "Login"
    # For the register button
    register_button_lct_link_text = "Register"


    # For the search field
    def enter_product_name_into_search_box_field(self,product_name):
        self.type_into_element(product_name,"search_box_field_lct_name",self.search_box_field_lct_name) # Used "type_into_element" method of BasePage

    # For the search icon
    def click_on_search_button(self):
        self.element_click("search_button_lct_xpath",self.search_button_lct_xpath) # Used "element_click" method of BasePage
        return SearchPage(self.driver) #Return the POM>>SearchPage.py page as an object

    # For the My Account button
    def click_on_the_my_account_button(self):
        self.element_click("my_account_button_lct_xpath",self.my_account_button_lct_xpath) # Used "element_click" method of BasePage

    # For the Login button
    def click_on_the_login_button(self):
        self.element_click("login_button_lct_link_text",self.login_button_lct_link_text) # Used "element_click" method of BasePage
        return LoginPage(self.driver) #Return the POM>>LoginPage.py page as an object

    # Merged tow method (click_on_the_my_account_button + click_on_the_login_button) in one method
    def navigate_to_login_page(self):
        self.click_on_the_my_account_button()
        return self.click_on_the_login_button()

    # For the register button
    def click_on_the_register_button(self):
        self.element_click("register_button_lct_link_text",self.register_button_lct_link_text) # Used "element_click" method of BasePage
        return RegisterPage(self.driver) #Return the POM>>RegisterPage.py file as an object

    # This method merged tow method (click_on_the_my_account_button + lick_on_the_register_button) to one method
    def navigate_to_register_page(self):
        self.click_on_the_my_account_button()
        return self.click_on_the_register_button()

    # This method is used for search product and after click on the search button
    def search_for_a_product(self,product_name):
        self.enter_product_name_into_search_box_field(product_name)
        return self.click_on_search_button()
