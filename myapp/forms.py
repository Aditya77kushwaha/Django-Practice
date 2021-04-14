from django import forms


class MyForm1(forms.Form):
    """Django Forms customized"""

    question = forms.CharField()
    choice = forms.BooleanField()
    pfp = forms.CharField()

    def __str__(self):
        return self.question
