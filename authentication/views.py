from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = 'sign-in.html'


class CustomLogOutView(TemplateView):
    template_name = 'log-out.html'


class RegisterView(View):
    def get(self, request):
        return render(request, 'sign-up.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'sign-up.html', {'form': form})
