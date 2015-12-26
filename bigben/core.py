from datetime import datetime, date
from django.utils import timezone

from django.conf import settings


class Clock(object):

    @classmethod
    def now(cls):
        if settings.BIGBEN_ENABLED:
            clockconfig = cls._get_clockconfig()
            if clockconfig is not None:
                return clockconfig.time
        return timezone.now()

    @classmethod
    def today(cls):
        return cls.now().date()

    @classmethod
    def set(cls, *args, time=None):
        if not settings.BIGBEN_ENABLED:
            raise ClockError(
                    'Cant set the time: bigben is disabled.')
        try:
            from .models import ClockConfig
            clockconfig = ClockConfig.objects.get()
            clockconfig.time = time if time else datetime(*args)
            clockconfig.save()
        except ClockConfig.DoesNotExist:
            ClockConfig.objects.create(time=time)

    @classmethod
    def _get_clockconfig(cls):
        try:
            from .models import ClockConfig
            return ClockConfig.objects.get()
        except ClockConfig.DoesNotExist:
            pass


class ClockError(Exception): pass
