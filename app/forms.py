from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class UserAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError("This Account is inactive. Talk to IT about activating your account",
                                  code='inactive', )
        pass


"""class PasswordChangeForm(AuthenticationForm):
    def PasswordChangeForm(self):
        pass


class PasswordResetForm(AuthenticationForm):
    def ResetPassword(self):
        pass"""