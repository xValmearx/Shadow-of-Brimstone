from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy, reverse

from .models import Character

class All_Characters(ListView):
    model = Character
    template_name = "All_Characters.html"

class Character_View(DetailView):
    model = Character

    def get_template_names(self):
         
         obj = self.get_object()
         
         return [f'{obj.character_class}_details.html']

    
    def get_success_url(self):
        obj = self.get_object()
        return reverse("character_detail", kwargs={"pk": obj.pk})
    


        
