from behave import given, when, then
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.search_page import SearchPage
from page_objects.signup_page import SignupPage
from utils.testutil import *


@given("I'm logged in with {username}")
def step_impl(context, username):
    driver = context.driver
    signup_page = SignupPage(driver)
    signup_page.click_on_link_to_login_page()

    login_page = LoginPage(driver)
    login_page.log_in_with_user_x(context.config[username])

    home_page = HomePage(driver)
    assert home_page.im_logged_in(context)


@when(u'I post a tweet with the text "{text_to_write}"')
def step_impl(context, text_to_write):
    context.tweet_text = text_to_write
    driver = context.driver
    home_page = HomePage(driver)
    home_page.tweetbox_region.post_tweet_with_text(text_to_write)


@then('I wait for it to appear on my dashboard')
def step_impl(context):
    driver = context.driver
    home_page = HomePage(driver)
    home_page.posted_tweets.wait_for_tweet_by_text(context.tweet_text)


@when('I delete the tweet with the same text')
def step_impl(context):
    driver = context.driver
    home_page = HomePage(driver)
    home_page.delete_tweet_by_element(context.tweet_text)


@then('It is no longer visible')
def step_impl(context):
    driver = context.driver
    home_page = HomePage(driver)
    home_page.posted_tweets.wait_for_tweet_to_disappear(context.tweet_text)
    context.tweet_text = None


@when('I hide the first tweet I see')
def step_impl(context):
    driver = context.driver
    home_page = HomePage(driver)
    tweet_element = home_page.posted_tweets.all_tweets[0]
    context.tweet_text = home_page.posted_tweets.get_tweet_text_by_element(tweet_element)
    home_page.posted_tweets.hide_tweet_by_element(tweet_element)


@when('I search for "{search_text}"')
def step_impl(context, search_text):
    driver = context.driver
    home_page = HomePage(driver)
    home_page.search_region.search_by_text(search_text)
    context.search_text = search_text


@when('I click on the {tab_name} tab')
def step_impl(context, tab_name):
    driver = context.driver
    search_page = SearchPage(driver)
    search_page.tabs.click_on_tab_by_text(tab_name)


@then('I see the user in the results')
def step_impl(context):
    driver = context.driver
    search_page = SearchPage(driver)
    search_page.wait_for_page_to_load()
    username = TwitterUsers.get_username_by_name(context.search_text)
    user_element = search_page.users.get_user_by_username(username)
    assert user_element is not None


@when("I type a tweet with {chars:d} characters")
def step_impl(context, chars):
    driver = context.driver
    home_page = HomePage(driver)
    tweet_text = "C" * chars
    home_page.tweetbox_region.type_text_to_tweet(tweet_text)


@then("I {action} post it")
def step_impl(context, action):
    driver = context.driver
    home_page = HomePage(driver)
    if action == "can":
        assert not home_page.tweetbox_region.submit_button_is_disabled()
    elif action == "can't":
        assert home_page.tweetbox_region.submit_button_is_disabled()
    else:
        print("No action item matches action: " + action)
        assert False


