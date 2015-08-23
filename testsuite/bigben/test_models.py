from datetime import datetime

from django.test import TestCase

from expecter import expect

from bigben.models import ClockConfig


class ClockConfigTest(TestCase):
    time = datetime(2020, 10, 10, 5, 30)

    def test_time_property(self):
        clockconfig = ClockConfig(time=self.time)
        clockconfig.save()

        expect(ClockConfig.objects.count()) == 1
        expect(ClockConfig.objects.get().time) == self.time
