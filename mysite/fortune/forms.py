from django import forms
from .models import Fortune

class FortuneForm(forms.ModelForm):
    class Meta:
        model = Fortune
        fields = ['title','text']

class ConnexionForm(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
