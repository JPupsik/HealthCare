from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from authentication.forms import LoginForm, RegisterForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'sign-in.html'


class CustomLogOutView(LogoutView):
    template_name = 'log-out.html'


class RegisterView(View):
    def get(self, request):
        return render(request, 'sign-up.html', {'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'sign-up.html', {'form': form})
