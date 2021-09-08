from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status')
        labels = {
            'title': gettext_lazy('Title'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status')
        }

        error_messages = {
            'title': {
                'required': gettext_lazy("Title is required."),
            },
            'description': {
                'required': gettext_lazy("Description is required."),
            },
        }
