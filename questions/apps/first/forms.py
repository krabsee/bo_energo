from django import forms
from .models import Color


class ColorForm(forms.Form):
    number = forms.CharField(max_length=3)


class CalculatorForm(forms.Form):
    first_coefficient = forms.CharField(max_length=50)
    second_coefficient = forms.CharField(max_length=50)
    third_coefficient = forms.CharField(max_length=50)
