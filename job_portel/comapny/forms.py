from django import forms
from .models import Comapny
class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model=Comapny
        exclude=('user',)