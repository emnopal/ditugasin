from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import View

from taskuserauth.forms import SignUpForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = '/'


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

        return render(request, self.template_name, {'form': form})

