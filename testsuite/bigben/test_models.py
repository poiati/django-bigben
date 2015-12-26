from datetime import datetime

from django.test import TestCase
from django.test.utils import override_settings
from django.utils import timezone

from expecter import expect

from bigben.models import ClockConfig


class ClockConfigTestExamples(object):

    def test_time_property(self):
        clockconfig = ClockConfig(time=datetime(2020, 10, 10, 5, 30))
        clockconfig.save()

        expect(ClockConfig.objects.count()) == 1
        expect(ClockConfig.objects.get().time) == self._expected_time()


@override_settings(USE_TZ=False)
class TZFalse_ClockConfigTest(ClockConfigTestExamples, TestCase):

    def _expected_time(self):
        return datetime(2020, 10, 10, 5, 30)


@override_settings(USE_TZ=True)
class TZTrue_ClockConfigTest(ClockConfigTestExamples, TestCase):

    def _expected_time(self):
        return timezone.make_aware(datetime(2020, 10, 10, 5, 30))
