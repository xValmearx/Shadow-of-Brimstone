# forms.py
from django import forms
from .models import Side_Bag, Character_Gear, Character_Mine_Artifact, Character_Targa_Artifact

class Add_Side_Bag_Token(forms.ModelForm):
    class Meta:
        model = Side_Bag
        fields = ['token','assigned_to_character']

class Add_Character_Gear(forms.ModelForm):
    class Meta:
        model = Character_Gear
        fields = ['gear','assigned_to_character']

class Add_Character_Mine_Artifact(forms.ModelForm):
    class Meta:
        model = Character_Mine_Artifact
        fields = ['mine_artifact','assigned_to_character']

class Add_Character_Targa_Artifact(forms.ModelForm):
    class Meta:
        model = Character_Targa_Artifact
        fields = ['targa_artifact','assigned_to_character']