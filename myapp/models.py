from django.db import models
from django.forms import ModelForm
# Create your models here.


class MyModel(models.Model):
    """Models for database"""
    question = models.CharField(max_length=100)
    choice = models.BooleanField(default=True)
    pfp = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class MyForm(ModelForm):
    """Form for respective Models"""
    class Meta:
        model = MyModel
        fields = ['question', 'choice', 'pfp']
