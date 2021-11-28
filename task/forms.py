from django.forms import DateTimeField, ModelForm, DateTimeInput
from django.utils.translation import gettext_lazy

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'status')
        labels = {
            'title': gettext_lazy('Title'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status'),
        }
        due_date = DateTimeField(
            label="Datetime format: Date/Month/Year Hour:Minute",
            input_formats=['%d/%m/%Y %H:%M'],
            label_suffix=" : ",
            widget=DateTimeInput(attrs={'class': 'datetimepicker'}),
            error_messages={'required': "This field is required."})

        error_messages = {
            'title': {
                'required': gettext_lazy("Title is required."),
            },
            'description': {
                'required': gettext_lazy("Description is required."),
            },
        }
