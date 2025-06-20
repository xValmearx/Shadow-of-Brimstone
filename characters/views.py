from django.views.generic import ListView,DetailView
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
import json

from .models import Character

class All_Characters(ListView):
    model = Character
    template_name = "All_Characters.html"
    

class Character_View(DetailView):
    model = Character

    def get_template_names(self):
         character = self.get_object()
         return f'{character.character_class}_details.html'
    
    def post(self, request, *args, **kwargs):
        character = self.get_object()
        context = {}

        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            key1 = data.get('key1')

            if key1 == 'health+':
                character.current_health += 1
                character.save()

                context["data"] = character.current_health
                return JsonResponse(context)
            elif key1 == "health-":
                character.current_health -= 1
                character.save()

                context["data"] = character.current_health
                return JsonResponse(context)

            context["data"] = "got data"
            return JsonResponse(context)
        except:
            context["error"] = "there seems to be an error"
            return JsonResponse(context)
    
    
    
    def get_success_url(self):
        obj = self.get_object()
        return reverse("character_detail", kwargs={"pk": obj.pk})
    


        
