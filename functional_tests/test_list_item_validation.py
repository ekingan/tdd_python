from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Emily goes to the homepage and accidentally tries to submit an empty list item.
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("id_new_item").send_keys(Keys.ENTER)
        # The homepage refreshes and there is an error message saying that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector(".has-error").text,
            "You cannot have an empty list item"
        ))
        # She tries again to enter text for the item and it works
        self.browser.find_element_by_id("id_new_item").send_keys("Buy carrots")
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy carrots")

        # Perversly she tries again to submit a blank item
        self.browser.find_element_by_id("id_new_item").send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector(".has-error").text, 
            "You cannot have an empty list item"
        ))

        # And she can correct it by filling some text in 
        self.browser.find_element_by_id("id_new_item").send_keys("Chop onions")
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy carrots")
        self.wait_for_row_in_list_table("2: Chop onions")
        self.fail('Finish the test!')
