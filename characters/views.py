from django.views.generic import ListView,DetailView
from django.urls import reverse
from django.http import JsonResponse
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
            # get data from the front end
            data = json.loads(request.body)

            # see what function we are preforming 
            function = data.get('function')

            if function == "update":
                if "health" in data.keys():
                    a = character.health + data["health"]
                    context["health"] = a
                    context["current_health"] = character.current_health
                    return JsonResponse(context)
                
                if "max_grit" in data.keys():
                    a = character.max_grit + data["max_grit"]
                    character.max_grit = a

                    if character.current_grit > character.max_grit:
                        character.current_grit = character.max_grit
                    character.save()

                    context["max_grit"] = a
                    context["current_grit"] = character.current_grit
                    return JsonResponse(context)

            if function == 'health+':
                if character.current_health < character.health:
                    character.current_health += 1
                    character.save()
                context["health"] = character.current_health
                return JsonResponse(context)
            
            elif function == "health-":
                if character.current_health > 0:
                    character.current_health -= 1
                    character.save()
                context["health"] = character.current_health
                return JsonResponse(context)
            
            elif function == 'sanity+':
                if character.current_sanity < character.sanity:
                    character.current_sanity += 1
                    character.save()
                context["sanity"] = character.current_sanity
                return JsonResponse(context)
            
            elif function == "sanity-":
                if character.current_sanity > 0:
                    character.current_sanity -= 1
                    character.save()
                context["sanity"] = character.current_sanity
                return JsonResponse(context)
            
            elif function == "grit+":
                if character.current_grit < character.max_grit:
                    character.current_grit += 1
                    character.save()
                context["grit"] = character.current_grit
                context["max_grit"] = character.max_grit
                return JsonResponse(context)
            
            elif function == "grit-":
                if character.current_grit > 0:
                    character.current_grit -= 1
                    character.save()
                context["grit"] = character.current_grit
                context["max_grit"] = character.max_grit
                return JsonResponse(context)
            
            elif function == "corupt+":
                if character.current_corruption < character.corruption:
                    character.current_corruption += 1
                    character.save()
                context["corruption"] = character.current_corruption
                return JsonResponse(context)
            
            elif function == "corupt-":
                if character.current_corruption > 0:
                    character.current_corruption -= 1
                    character.save()
                context["corruption"] = character.current_corruption
                return JsonResponse(context)
            
            elif function == "card_next":
                character.class_card += 1

                if character.class_card > 3:
                    character.class_card = 1
                character.save()
                context["card"] = character.class_card
                return JsonResponse(context)
            
            elif function == "card_previous":
                character.class_card -= 1

                if character.class_card < 1:
                    character.class_card = 3
                character.save()
                context["card"] = character.class_card
                return JsonResponse(context)
            
            context["data"] = "got data"
            return JsonResponse(context)
        
        except:
            context["error"] = "there seems to be an error"
            return JsonResponse(context)


    
    def get_success_url(self):
        obj = self.get_object()
        return reverse("character_detail", kwargs={"pk": obj.pk})
    