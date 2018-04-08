from extendedwebdriver import ExtendedWebdriver
import configparser


def before_all(context):
    config = configparser.ConfigParser()
    config.read('config_prod_chrome.ini')
    context.config = config


def before_scenario(context, scenario):
    context.extended_webdriver = ExtendedWebdriver()
    context.driver = context.extended_webdriver.driver
    context.extended_webdriver.go_to_base_url()


def after_scenario(context, scenario):
    context.extended_webdriver.teardown()
