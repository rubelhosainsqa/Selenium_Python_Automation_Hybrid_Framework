import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.HomePage import HomePage
from POM.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearchProduct:

   # Test Case 1 (Positive Test Case)
   def test_search_with_valid_product(self):
      home_page = HomePage(self.driver)
      search_page = home_page.search_for_a_product("HP")
      assert search_page.display_status_of_hp_product()


   # Test Case 2 (Negative Test Case)
   def test_search_with_invalid_product(self):
      home_page = HomePage(self.driver)
      search_page = home_page.search_for_a_product("Tiger")
      expected_text = "There is no product that matches the search criteria."
      assert search_page.no_result_text_message().__eq__(expected_text)


   # Test Case 3 (Negative Test Case)
   def test_search_with_blank_product(self):
      home_page = HomePage(self.driver)
      search_page = home_page.search_for_a_product("")
      expected_text = "There is no product that matches the search criteria."
      assert search_page.no_result_text_message().__eq__(expected_text)
