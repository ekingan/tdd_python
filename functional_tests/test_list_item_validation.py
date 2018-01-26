from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Emily goes to the homepage and accidentally tries to submit an empty list item.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request and does not load the list page
        self.wait_for(lambda: self.browser.find_element_by_css_selector("#id_text:invalid"))

        # She begins to enter text for the item and the error message disappears
        self.get_item_input_box().send_keys("Buy carrots")
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:valid'))

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy carrots")

        # Perversly she tries again to submit a blank item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again the browser will not comply
        self.wait_for_row_in_list_table("1: Buy carrots")
        self.wait_for(lambda: self.browser.find_element_by_css_selector("#id_text:invalid")) 

        # And she can correct it by filling some text in 
        self.get_item_input_box().send_keys("Chop onions")
        self.wait_for(lambda: self.browser.find_element_by_css_selector("#id_text:valid"))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy carrots")
        self.wait_for_row_in_list_table("2: Chop onions")
