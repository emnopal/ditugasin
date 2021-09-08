from django import forms
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        labels = {
            'username': gettext_lazy('Username'),
            'first_name': gettext_lazy('First Name'),
            'last_name': gettext_lazy('Last Name'),
            'email': gettext_lazy('Email')
        }
