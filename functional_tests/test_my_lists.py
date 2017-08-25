
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest
from .list_page import ListPage


import time

User = get_user_model()


class MyListsTest(FunctionalTest):



    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged in user
        email = 'edith@example.com'
        self.create_pre_authenticated_session(email)

        # She goes to the home page and starts a list
        self.browser.get(self.live_server_url)
        list_page = ListPage(self).add_list_item('Immanentize eschaton')
        list_page.add_list_item('Reticulate splines')

        first_list_url = self.browser.current_url

        # She notices a "My Lists" link, for the first time
        self.browser.find_element_by_link_text('My lists').click()

        # She sees that her list is in there, named according to its
        # first list item
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Immanentize eschaton')
        )
        self.browser.find_element_by_link_text('Immanentize eschaton').click()
        self.wait_for(
            lambda: self.assertEqual(first_list_url, self.browser.current_url)
        )

        # She decides to start another list, just to see
        self.browser.get(self.live_server_url)
        list_page = ListPage(self).add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Under "My Lists", her new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # She logs out. The "My lists" option disappears
        self.browser.find_element_by_link_text('Log Out').click()
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_elements_by_link_text('My lists'), []
            )
        )
