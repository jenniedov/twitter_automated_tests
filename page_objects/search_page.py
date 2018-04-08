from pypom import Region
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):

    @property
    def tabs(self):
        return self.Tabs(self)

    @property
    def users(self):
        return self.Users(self)

    class Tabs(Region):

        _tab = (By.CSS_SELECTOR, "li.AdaptiveFiltersBar-item.u-borderUserColor")
        _tab_text = (By.TAG_NAME, "a")

        @property
        def all_tabs(self):
            return self.find_elements(*self._tab)

        def click_on_tab_by_text(self, text):
            for tab in self.all_tabs:
                tab_name = self.get_tab_name_by_element(tab)
                if text in tab_name:
                    tab.click()

        def get_tab_name_by_element(self, element):
            return element.find_element(*self._tab_text).text

    class Users(Region):

        _user_locator = (By.CSS_SELECTOR, "div[data-item-type='user']")
        _username_text = (By.CSS_SELECTOR, "b.u-linkComplex-target")

        @property
        def all_users(self):
            return self.find_elements(*self._user_locator)

        def get_username_str_by_element(self, element):
            return element.find_element(*self._username_text).text

        def get_user_by_username(self, username):
            user_element= None
            for user in self.all_users:
                username_text = self.get_username_str_by_element(user)
                if username in username_text:
                    user_element = user
            return user_element
