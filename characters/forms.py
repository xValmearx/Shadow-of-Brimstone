# forms.py
from django import forms
from .models import Side_Bag

class Add_Side_Bag_Token(forms.ModelForm):
    class Meta:
        model = Side_Bag
        fields = ['token','assigned_to_character']