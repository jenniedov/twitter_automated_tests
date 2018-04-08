from selenium.webdriver.common.by import By
from pypom import Page


class SignupPage(Page):

    URL_TEMPLATE = "https://twitter.com/signup"

    # Locators
    _login_link = (By.LINK_TEXT, "Log in")
    _signup_button = (By.ID, "submit_button")
    _email_field = (By.ID, "email")
    _password_field = (By.ID, "password")
    _name_field = (By.ID, "full-name")

    # Simple method
    def click_on_link_to_login_page(self):
        login_link_element = self.find_element(*self._login_link)
        login_link_element.click()

    def type_email(self , email):
        email_field = self.find_element(*self._email_field)
        email_field.send_keys(email)

    def type_password(self, password):
        password_field = self.find_element(*self._password_field)
        password_field.send_keys(password)

    def type_name(self, name):
        name_field = self.find_element(*self._name_field)
        name_field.send_keys(name)

    def click_signup_button(self):
        signup_button = self.find_element(*self._signup_button)
        signup_button.click()

    # Complex methods
    def signup_with_user(self, user):
        self.type_name(user["name"])
        self.type_email(user["email"])
        self.type_password(user["password"])
        self.click_signup_button()


