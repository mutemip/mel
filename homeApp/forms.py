from dataclasses import field
from .models import HomeApp
from django.forms import ModelForm
from django import forms

class HomeForm(ModelForm):
    home = forms.CharField(label="Home", max_length=255)
    age = forms.IntegerField(label="Age")
    salary = forms.IntegerField(label="Salary")

    class Meta:
        model = HomeApp
        fields = '__all__'