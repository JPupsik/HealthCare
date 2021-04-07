import unicodedata

from django.contrib.auth.models import User
from django.contrib.auth import password_validation, validators
from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                           'class': 'form-control',
                                                           'id': 'username'}, ))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'form-control',
                                          'id': 'password'}), )


class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
            'class': 'form-control',
            'id': 'username'
        }


class RegisterForm(UserCreationForm):
    email = forms.CharField(
        label=_("Email"),
        strip=False,
        widget=forms.EmailInput(attrs={'autocomplete': 'on',
                                       'class': 'form-control',
                                       'id': 'email'}),
        help_text=EmailValidator(),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'id': 'password1'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'id': 'password2'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
