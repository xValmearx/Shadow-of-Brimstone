# forms.py
from django import forms
from .models import Side_Bag, Character_Gear

class Add_Side_Bag_Token(forms.ModelForm):
    class Meta:
        model = Side_Bag
        fields = ['token','assigned_to_character']

class Add_Character_Gear(forms.ModelForm):
    class Meta:
        model = Character_Gear
        fields = ['gear','assigned_to_character']