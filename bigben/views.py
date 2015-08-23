from datetime import datetime

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django import forms

from bigben import Clock


DATETIME_FORMAT = '%Y-%m-%d %H:%M'


class SetTimeForm(forms.Form):
    current_time = forms.DateTimeField(input_formats=[DATETIME_FORMAT])


class SetTimeFormView(FormView):
    form_class = SetTimeForm
    template_name = 'set_time.html'
    success_url = reverse_lazy('set_time')

    def get_context_data(self, *args, **kwargs):
        context = super(SetTimeFormView, self).get_context_data(*args, **kwargs)
        context['current_time'] = Clock.now().strftime(DATETIME_FORMAT)
        return context

    def form_valid(self, form):
        Clock.set(form.cleaned_data['current_time'])
        return super(SetTimeFormView, self).form_valid(form)
