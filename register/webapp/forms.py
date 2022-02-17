from django import forms
from .models import Userdata


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userdata
        fields = (
            'username', 'password'
        )


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userdata
        fields = (
            'first_name', 'last_name', 'date_of_birth', 'username', 'address', 'email_id',
            'phone','password', 'confirm_password'
        )

