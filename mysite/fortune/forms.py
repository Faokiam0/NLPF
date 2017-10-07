from django import forms
from .models import Fortune

class FortuneForm(forms.ModelForm):
    class Meta:
        model = Fortune
        fields = ['title','text']