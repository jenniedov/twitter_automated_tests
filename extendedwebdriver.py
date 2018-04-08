from selenium import webdriver
import configparser

class ExtendedWebdriver():

    config = configparser.ConfigParser()
    config.read('config_prod_chrome.ini')
    driver = None

    def __init__(self):
        self.get_webdriver()

    def get_webdriver(self):
        if self.driver == None:
            browser_type = self.config['Driver']['browser']
            browser_path = self.config['Driver']['driver_path']
            if browser_type == "Chrome":
                self.driver = webdriver.Chrome(browser_path)
            elif browser_type == "FireFox":
                pass #TODO: implement firefox webdriver
            elif browser_type == "IE":
                pass #TODO: implement IE webdriver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver



    def teardown(self):
        self.driver.quit()
        self.driver = None

    def go_to_base_url(self):
        self.driver.get(self.config["env"]["base_url"])

    def does_element_exist(self , By_element ):
        if len(self.driver.find_elements(*By_element)):
            return True
        else :
            return False


#wait for element method


