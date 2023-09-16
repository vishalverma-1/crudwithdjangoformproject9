from django import forms
from django.forms import ModelForm
from .models import sexy
class sexyform(forms.ModelForm):
    class Meta:
        model=sexy
        fields="__all__"