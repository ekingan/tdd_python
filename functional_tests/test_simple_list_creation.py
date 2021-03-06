from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Emily has heard about a cool new online to-do app. She goes to check out the home page.
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item right away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and the page lists
        # "!: buy peacock feathers" as an item on the to-do lists
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add an item, she enters
        # "Use feathers to make a fly"
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use feathers to make a fly')
        # She hits enter again and sees the second to-do item on her lists
        inputbox.send_keys(Keys.ENTER)
        # The page updates again and she sees both items in her list
        self.wait_for_row_in_list_table('2: Use feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She visits that url and sees that her to-do list is still there

        # Satisfied she goes back to sleep
    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Emily see there is a special url for her list
        emily_list_url = self.browser.current_url
        self.assertRegex(emily_list_url, '/lists/.+')
    
        # Now a new user, Francis, comes to the site

        ## User a new browser session to assure no information of Emily's is coming through from cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Emily's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make a fly', page_text)

        # Francis starts a new list by entering an item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy chocolate')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy chocolate')

        # Francis gets his own unique url
        francis_list_url = self.browser.current_url

        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, emily_list_url)

        # Again there is no trace of Emily's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy chocolate', page_text)

        # Satisfied they both go to sleep

