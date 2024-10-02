from django import forms
from .models import FILME

class FilmeModelForm(forms.ModelForm):
    class Meta:
        model = FILME
        fields = '__all__'