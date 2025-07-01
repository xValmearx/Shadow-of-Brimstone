from django.views.generic import ListView,DetailView,CreateView,TemplateView
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import Add_Side_Bag_Token


import json

from .models import Character, Side_Bag

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
            
            elif function == 'gold':
                a = character.gold + int(data["gold_value"])
                character.gold = a
                character.save()

                context["new_gold_value"] = character.gold
                return JsonResponse(context)
            
            elif function == 'dark_stone':
                if data['dark_stone_value'] == '+':
                    character.dark_stone += 1
                elif data['dark_stone_value'] == '-' and character.dark_stone > 0:
                    character.dark_stone -= 1
                character.save()

                context["new_dark_stone_value"] = character.dark_stone
                return JsonResponse(context)

            elif function == "XP":
                a = character.xp + int(data["xp_value"])
                character.xp = a
                character.save()

                context["new_xp_value"] = character.xp
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
            
            elif function == 'delete_token':
                pk = data["token_instnace"]

                instance = get_object_or_404(Side_Bag, pk=pk)
                instance.delete()

                context["data"] = "deleted_token"
                
                return JsonResponse(context)

        except:
            context["error"] = "there seems to be an error"
            return JsonResponse(context)
        
    
    def get_object(self, queryset=None):
        # Fetch the object fresh from the database
        obj = super().get_object(queryset)
        return Character.objects.get(pk=obj.pk)


    def get_success_url(self):
        obj = self.get_object()
        return reverse("character_detail", kwargs={"pk": obj.pk})
    
class Create_Side_Bag_Token(CreateView):
    
    model = Side_Bag
    form_class = Add_Side_Bag_Token
    template_name = "new_side_bag_token.html"

    def get_initial(self):
        initial = super().get_initial()
        # Retrieve the URL parameter (e.g., pk)
        pk = self.kwargs.get('pk')
        if pk:
            # Fetch data from the database or set initial values
            try:
                obj = Character.objects.get(pk=pk)
                initial['assigned_to_character'] = obj  # Pre-fill form field
            except Character.DoesNotExist:
                pass
        return initial

    def form_valid(self, form):
        # Process the form data
        return super().form_valid(form)


    def get_success_url(self):
        # Dynamically generate the success URL

        return self.object.get_absolute_url()
    
    

