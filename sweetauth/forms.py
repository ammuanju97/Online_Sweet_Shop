from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SweetUserForm(UserCreationForm):
    
    first_name = forms.CharField(max_length = 30, required = False)
    last_name = forms.CharField(max_length = 30, required = False)
    email = forms.EmailField(max_length = 254)
    username = forms.CharField(max_length = 30, required = False)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')