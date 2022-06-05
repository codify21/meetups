from django import forms
from .models import Users

# from .models import Participant

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model =  Participant
#         fields = ['email']

class RegistrationForm(forms.Form):
    email = forms.EmailField(label = 'Your Email')

class LoginForm(forms.Form):
    email = forms.EmailField(label = 'Your Email')
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = Users
    #     fields = [ 'email', 'password'] 
    
    #     widgets = {
    #     'password': forms.PasswordInput()
    #      }