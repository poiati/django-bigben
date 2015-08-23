from django.conf.urls import patterns, url

from bigben.views import SetTimeFormView


urlpatterns = patterns('',
    url(r'^bigben/$', SetTimeFormView.as_view(), name='set_time'),
)
