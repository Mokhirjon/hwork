from django import forms
from .models import OurModel


class Ourforms(forms.ModelForm):
    name_uz = forms.CharField()
    name_ru = forms.CharField(required=False)
    name_en = forms.CharField(required=False)

    fname_uz = forms.CharField()
    fname_ru = forms.CharField(required=False)
    fname_en = forms.CharField(required=False)

    text_uz = forms.CharField()
    text_ru = forms.CharField(required=False)
    text_en = forms.CharField(required=False)

    class Meta:
        model = OurModel
        exclude = ['name', 'fname', 'text']
