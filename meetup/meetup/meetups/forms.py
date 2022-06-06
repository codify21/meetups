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
    email = forms.EmailField(label = 'Email')
    password = forms.CharField(initial='*******',widget=forms.PasswordInput())



# class LoginForm(forms.ModelForm):

#     class Meta:
#         model = Users
#         fields = [ 'email', 'password'] 
#         labels = {
#             'email':'Your Email',
#             'password':'Password'
#         }
    
#         widgets = {
#         'password': forms.PasswordInput()
#          }