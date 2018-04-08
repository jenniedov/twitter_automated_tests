from selenium.webdriver.common.by import By
from pypom import Page


class LoginPage(Page):

    # Locators
    email_field = (By.CSS_SELECTOR, "input.js-username-field.email-input.js-initial-focus")
    password_field = (By.CSS_SELECTOR , "input.js-password-field")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    # Simple methods
    def fill_email_field(self, email):
        email_field_element = self.find_element(*self.email_field)
        email_field_element.send_keys(email)

    def fill_password_field(self, password):
        password_field_element = self.find_element(*self.password_field)
        password_field_element.send_keys(password)

    def click_submit_button(self):
        button_element = self.find_element(*self.submit_button)
        button_element.click()

    # Complex methods
    def log_in_with_user_x(self, user_config):
        LoginPage.fill_email_field(self, user_config["email"])
        LoginPage.fill_password_field(self, user_config["password"])
        LoginPage.click_submit_button(self)

