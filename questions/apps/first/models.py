from django.db import models


class Color(models.Model):
    number = models.CharField(max_length=3)


class CalculatorForm(models.Model):
    first_coefficient = models.CharField(max_length=50)
    second_coefficient = models.CharField(max_length=50)
    third_coefficient = models.CharField(max_length=50)
