from datetime import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse

from expecter import expect

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from bigben import Clock, views


class SetTimeFormViewTest(TestCase):

    def test_get(self):
        response = self.client.get(self._reverse())

        expect(response.status_code) == 200
        expect(response.context['current_time']) != None

    @patch('bigben.views.Clock', spec=Clock)
    def test_post_valid_data(self, clock_mock):
        current_time = '2015-10-11 15:20'
        response = self.client.post(
                self._reverse(), 
                {'current_time': current_time})

        clock_mock.set.assert_called_with(
                datetime.strptime(current_time, views.DATETIME_FORMAT))

    def _reverse(self):
        return reverse('set_time')
