from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['image', 'education', 'qualities', 'abilities', 'awards']
    education = forms.CharField(required=False)
    awards = forms.CharField(required=False)

