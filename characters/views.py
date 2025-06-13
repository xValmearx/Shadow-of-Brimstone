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

         if obj.character_class == "Marshal":
             return ['marshal_details.html']


          # if Character.character_class == "Rancher":
          #      template_name = "rancher_details.html"
          
          # if Character.character_class == "LawMan":
          #      template_name = "lawman_details.html"
          
          # if Character.character_class == "PianoPlayer/SaloonGirl":
          #      template_name = "pianoplayer_saloongirl_details.html"
          
          # if Character.character_class == "IndianScout":
          #      template_name = "indianscout_details.html"

          # if Character.character_class == "Bandido":
          #      template_name = "bandido_details.html"

          # if Character.character_class == "Preacher":
          #      template_name = "preacher_details.html"

          # if Character.character_class == "GunSlinger":
          #      template_name = "gunslinger_details.html"
    
    def get_success_url(self):
        twit = self.get_object()
        return reverse("character_detail", kwargs={"pk": twit.pk})
    


        
