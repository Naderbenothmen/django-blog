from django import forms
from .models import User, Machine


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    password = forms.CharField(widget=forms.PasswordInput())


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'location', 'description']