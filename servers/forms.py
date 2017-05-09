from .models import Server
from django.forms import ModelForm
from django import forms

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'ip', 'order']
        widgets = {
            'name' : forms.TextInput(attrs = {'size':'20'}),
            'ip' : forms.TextInput(attrs = {'size':'20'}),
            'order' : forms.TextInput(attrs = {'size':'20'}),
        }
