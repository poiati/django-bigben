import time

from datetime import datetime

from django.test import LiveServerTestCase
from django.utils.formats import localize

from selenium import webdriver
from expecter import expect

from bigben.views import DATETIME_FORMAT


class FunctionalTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.PhantomJS()       
        super(FunctionalTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(FunctionalTest, cls).tearDownClass()

    def test_set_the_hour(self):
        self.browser.get(self.live_server_url + '/bigben/')

        now = datetime.now()
        expect(self.browser.page_source).contains('%s' % now.strftime(DATETIME_FORMAT))

        new_current_datetime = '1985-05-15 02:10'
        datetime_input = self.browser.find_element_by_name('current_time')
        datetime_input.send_keys(new_current_datetime)

        submit_button = self.browser.find_element_by_tag_name('button')
        submit_button.click()

        expect(self.browser.page_source).contains(new_current_datetime)
