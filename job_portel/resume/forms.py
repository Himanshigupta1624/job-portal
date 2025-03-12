from django import forms
from .models import REsume


class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model=REsume
        exclude=('user',)