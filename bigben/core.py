from datetime import datetime, date

from django.conf import settings

from .models import ClockConfig


class Clock(object):

    @classmethod
    def now(cls):
        if settings.BIGBEN_ENABLED:
            clockconfig = cls._get_clockconfig()
            if settings.BIGBEN_ENABLED and clockconfig is not None:
                return clockconfig.time
        return datetime.now()

    @classmethod
    def today(cls):
        if settings.BIGBEN_ENABLED:
            clockconfig = cls._get_clockconfig()
            if clockconfig is not None:
                return clockconfig.time.date()
        return date.today()

    @classmethod
    def set(cls, time):
        if not settings.BIGBEN_ENABLED:
            raise ClockError(
                    'You must be running Django in DEBUG mode to set the time')
        try:
            clockconfig = ClockConfig.objects.get()
            clockconfig.time = time
            clockconfig.save()
        except ClockConfig.DoesNotExist:
            ClockConfig.objects.create(time=time)

    @classmethod
    def _get_clockconfig(cls):
        try:
            return ClockConfig.objects.get()
        except ClockConfig.DoesNotExist:
            pass


class ClockError(Exception): pass
