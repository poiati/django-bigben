from datetime import datetime, date, timedelta

from django.test import TestCase
from django.test.utils import override_settings
from django.utils import timezone

from expecter import expect

from bigben import Clock, ClockError
from bigben.models import ClockConfig


class ClockTest(TestCase):
    faketime = datetime(2020, 10, 10, 5, 30)


@override_settings(BIGBEN_ENABLED=True)
class EnableClockTestCase(ClockTest):

    def setUp(self):
        super(EnableClockTestCase, self).setUp()

        ClockConfig.objects.create(time=self.faketime)

    def test_now(self):
        expect(Clock.now()) == self.faketime

    def test_today(self):
        expect(Clock.today()) == self.faketime.date()

    def test_set_time(self):
        Clock.set(time=self.faketime)

        expect(ClockConfig.objects.get().time) == self.faketime

        othertime = self.faketime + timedelta(days=3)
        Clock.set(time=othertime)

        expect(ClockConfig.objects.get().time) == othertime

    def test_set_time_with_args(self):
        Clock.set(2020, 10, 11)

        expect(ClockConfig.objects.get().time) == datetime(2020, 10, 11)


@override_settings(BIGBEN_ENABLED=False)
class DisableClockTestCase(ClockTest):

    def test_now(self):
        expect(Clock.now()) <= timezone.now()

    def test_today(self):
        expect(Clock.today()) == timezone.now().date()

    def test_now_faketime_set(self):
        ClockConfig.objects.create(time=self.faketime)

        expect(Clock.now()) <= timezone.now()

    def test_today_faketime_set(self):
        ClockConfig.objects.create(time=self.faketime)

        expect(Clock.today()) == timezone.now().date()

    def test_set_time(self):
        with expect.raises(ClockError):
            Clock.set(time=self.faketime)
