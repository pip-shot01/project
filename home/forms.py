from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =  ['full_name','last_name','email','phone','message']

        

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1','password2')

STATE = [
    ('Abia','Abia'),
    ('Delta','Delta'),
    ('Edo','Edo'),
    ('Usa','Usa'),
    ('Imo','Imo'),
    ('Lagos','Lagos'),
    ('Ogun','Ogun'),
    ('Ondo','Ondo')
]
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','phone','address','state','pix']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone number'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'your address'}),
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'your state'}, choices=STATE),
            'pix':forms.FileInput(attrs={'class':'form-control'})
        }
       
       
class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity']

