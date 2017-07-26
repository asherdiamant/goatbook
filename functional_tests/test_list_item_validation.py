from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTests(FunctionalTest):

	def test_cannot_add_empty_list_item(self):
		# Edith goes to the home page and accidentaly tries to submit
		# an empty to-do item. She hits Enter on the empty input box 

		# The home page refreshes, and there is an error message saying
		# that list itmes cannot be blank

		# She tries again with some text for the item which now works

		# Perversely, she now decides to submit a second blank list item

		# She receives a similar warning on the list page

		# And she can correct it by filling some text in

		self.fail('Write me!')
