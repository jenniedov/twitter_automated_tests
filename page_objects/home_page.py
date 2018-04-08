from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from pypom import Region


class HomePage(BasePage):

    URL_TEMPLATE = "https://twitter.com/"

    def delete_tweet_by_element(self, text):
        tweet_element = self.posted_tweets.get_tweet_element(text)
        self.posted_tweets.click_on_tweet_dropdown_by_element(tweet_element)
        self.posted_tweets.click_delete_by_tweet_element(tweet_element)
        self.delete_popup.confirm_delete_tweet()

    # Regions
    @property
    def tweetbox_region(self):
        return self.TweetboxRegion(self)

    @property
    def posted_tweets(self):
        return self.PostedTweetsRegion(self)

    @property
    def delete_popup(self):
        return self.DeletePopup(self)



    class TweetboxRegion(Region):
        _root_locator = (By.CSS_SELECTOR, "div.timeline-tweet-box")
        _tweet_box = (By.ID, "tweet-box-home-timeline")
        _submit_tweet_button = (By.CSS_SELECTOR, "button>span.button-text.tweeting-text")
        _disabled_submit = (By.CSS_SELECTOR, "button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn[disabled]")

        def type_text_to_tweet(self, text_to_write):
            tweet_box = self.find_element(*self._tweet_box)
            tweet_box.clear()
            tweet_box.send_keys(text_to_write)

        def click_submit_button(self):
            submit_button = self.find_element(*self._submit_tweet_button)
            submit_button.click()

        def post_tweet_with_text(self, text_to_write):
            self.type_text_to_tweet(text_to_write)
            self.click_submit_button()

        def submit_button_is_disabled(self):
            try:
                self.find_element(*self._disabled_submit)
                return True
            except NoSuchElementException:
                return False

    class PostedTweetsRegion(Region):

        _root_locator = (By.CSS_SELECTOR, "div.stream-container.conversations-enabled ")
        _tweet_locator = (By.CSS_SELECTOR, "div.content")
        _text_in_tweet = (By.CSS_SELECTOR, "div.js-tweet-text-container>p")
        _dropdown_tweet = (By.CSS_SELECTOR, "span.Icon.Icon--caretDownLight.Icon--small" )
        _delete_tweet = (By.CSS_SELECTOR, "li.js-actionDelete>button")
        _hide_tweet = (By.CSS_SELECTOR, "li>button[data-feedback-type='DontLike']")
        _like_tweet = (By.CSS_SELECTOR, "div.HeartAnimation")
        _like_count_is_zero = (By.CSS_SELECTOR, "span.ProfileTweet-actionCount.ProfileTweet-actionCount--isZero")
        _like_count = (By.CSS_SELECTOR, "button.ProfileTweet-actionButton.js-actionButton.js-actionFavorite>span")

        @property
        def all_tweets(self):
            return self.find_elements(*self._tweet_locator)

        def get_tweet_element(self, text):
            tweet_element = None
            for tweet in self.all_tweets:
                tweet_text = self.get_tweet_text_by_element(tweet)
                if text in tweet_text:
                    tweet_element = tweet
            return tweet_element

        def tweet_is_visible(self, text):
            return self.get_tweet_element(text) is not None

        def wait_for_tweet_by_text(self, text):
            # The default explicit wait in pypom is 10 secs.
            # I can change it to another value by overriding the __init__ of the page/region.
            self.wait.until(lambda s: self.tweet_is_visible(text))

        def wait_for_tweet_to_disappear(self, text):
            self.wait.until_not(lambda s: self.tweet_is_visible(text))

        def get_tweet_text_by_element(self, element):
            return element.find_element(*self._text_in_tweet).text

        def click_on_tweet_dropdown_by_element(self, element):
            dropdown_element = element.find_element(*self._dropdown_tweet)
            dropdown_element.click()

        def click_delete_by_tweet_element(self, element):
            delete_link = element.find_element(*self._delete_tweet)
            delete_link.click()

        def click_hide_by_tweet_element(self, element):
            hide_link = element.find_element(*self._hide_tweet)
            hide_link.click()

        def hide_tweet_by_element(self, element):
            self.click_on_tweet_dropdown_by_element(element)
            self.click_hide_by_tweet_element(element)




    class DeletePopup(Region):

        _delete_tweet_button = (By.CSS_SELECTOR, "div>button.EdgeButton.EdgeButton--danger.delete-action")

        def confirm_delete_tweet(self):
            delete_button = self.find_element(*self._delete_tweet_button)
            delete_button.click()