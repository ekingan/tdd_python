from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        #Emily has heard about a cool new online to-do app. She goes to check out the home page.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item right away

        # She types "buy peacock feathers" into a text box

        # When she hits enter, the page updates, and the page lists
        # "!: buy peacock feathers" as an item on the to-do lists

        # There is still a text box inviting her to add an item, she enters
        # "Use feathers to make a fly"

        # She hits enter again and sees the second to-do item on her lists

        # Emily see there is a special url for her list

        # She visits that url and sees that her to-do list is still there

        # Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
