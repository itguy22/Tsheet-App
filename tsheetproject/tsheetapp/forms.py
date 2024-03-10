from django import forms
from .models import TSheet

class TSheetForm(forms.ModelForm):
    class Meta:
        model = TSheet
        fields = ['headline', 'image']

