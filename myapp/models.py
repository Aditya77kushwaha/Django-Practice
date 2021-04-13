from django.db import models

# Create your models here.


class MyModel(models.Model):
    """Models for database"""
    question = models.CharField(max_length=100)
    choice = models.BooleanField(default=True)
    pfp = models.CharField(max_length=250)

    def __str__(self):
        return self.question
