from selenium.webdriver.common.by import By
from pypom import Page, Region


class BasePage(Page):
    """ Base object for logged-in pages """

    # page methods
    def im_logged_in(self, context):
        return self.user_region.user_icon_exists(context)
        # It's possible to add more parameters to assert that i'm logged in.

    @property
    def user_region(self):
        return self.UserRegion(self)

    @property
    def search_region(self):
        return self.SearchRegion(self)

    # Regions
    class UserRegion(Region):
        _root_locator = (By.CLASS_NAME, "nav right-actions")
        _user_icon = (By.ID, "user-dropdown-toggle")
        _log_out_link = None  # TODO: implement
        _settings_link = None  # TODO: implement
        _profile_link = None  # TODO: implement

        def user_icon_exists(self, context):
            return context.extended_webdriver.does_element_exist(self._user_icon)

    class SearchRegion(Region):
        _root_locator = (By.CSS_SELECTOR, "div[role='search']")
        _search_box = (By.ID, "search-query")
        _submit_button = (By.CSS_SELECTOR, "button[type='submit']")

        def type_text_in_serach_box(self, text):
            search_box = self.find_element(*self._search_box)
            search_box.send_keys(text)

        def submit_search(self):
            submit_button = self.find_element(*self._submit_button)
            submit_button.click()

        def search_by_text(self, text):
            self.type_text_in_serach_box(text)
            self.submit_search()
