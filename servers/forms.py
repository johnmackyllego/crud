from .models import Server
from django.forms import ModelForm
from django import forms

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'address', 'mobile']
        widgets = {
            'name' : forms.TextInput(attrs = {'size':'20'}),
            'address' : forms.TextInput(attrs = {'size':'20'}),
            'mobile' : forms.TextInput(attrs = {'size':'20'}),
        }
