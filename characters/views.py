from django.views.generic import ListView,DetailView,CreateView,TemplateView
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import Add_Side_Bag_Token, Add_Character_Gear, Add_Character_Mine_Artifact, Add_Character_Targa_Artifact

import json

from .models import Character, Side_Bag, Character_Gear, Character_Mine_Artifact, Character_Targa_Artifact

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

            # if the function is updating the character stats
            if function == "update":

        # Update the characters agility based on the value associated with the 'agility' key in the data dictionary
                if 'agility' in data.keys():
                    a = character.agility + int(data['agility'])
                    character.agility = a
                    character.save()

                    context['luck'] = character.agility
                    character.save()

        # Update the characters cunning based on the value associated with the 'cunning' key in the data dictionary
                if 'cunning' in data.keys():
                    a = character.cunning + int(data['cunning'])
                    character.cunning = a
                    character.save()

                    context['cunning'] = character.cunning
                    character.save()

        # Update the characters spirit based on the value associated with the 'spirit' key in the data dictionary
                if 'spirit' in data.keys():
                    a = character.spirit + int(data['spirit'])
                    character.spirit = a
                    character.save()

                    context['spirit'] = character.spirit
                    character.save()

        # Update the characters strength based on the value associated with the 'strength' key in the data dictionary
                if 'strength' in data.keys():
                    a = character.strength + int(data['strength'])
                    character.strength = a
                    character.save()

                    context['strength'] = character.strength
                    character.save()

        # Update the characters lore based on the value associated with the 'lore' key in the data dictionary
                if 'lore' in data.keys():
                    a = character.lore + int(data['lore'])
                    character.lore = a
                    character.save()

                    context['lore'] = character.lore
                    character.save()

        # Update the characters luck based on the value associated with the 'luck' key in the data dictionary
                if 'luck' in data.keys():
                    a = character.luck + int(data['luck'])
                    character.luck = a
                    character.save()

                    context['luck'] = character.luck
                    character.save()
                
        # Update the characters health based on the value associated with the 'luck' key in the data dictionary
                if "health" in data.keys():
                    a = character.health + data["health"]
                    context["health"] = a
                    context["current_health"] = character.current_health
                    character.health = a
                    
                    character.save()
                    
                
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
            
            elif function == 'delete_gear':
                pk = data["gear_instance"]
                instance = get_object_or_404(Character_Gear, pk=pk)
                instance.delete()

                context["data"] = "deleted_gear"
                return JsonResponse(context)
            
            elif function == "equip_gear_instance":
                pk = data["gear_instance"]
                instance = get_object_or_404(Character_Gear,pk = pk)
                instance.equiped = True

                instance.save()

                context['equiped'] = 'a'
                return JsonResponse(context)

            elif function == "equip_mine_artifact_instance":
                pk = data['mine_artifact_instance']
                instance = get_object_or_404(Character_Mine_Artifact,pk = pk)
                instance.equiped = True

                instance.save()

                context['equiped'] = 'a'
                return JsonResponse(context)

            elif function == "delete_mine_artifact":
                pk = data['mine_artifact_instance']
                instance = get_object_or_404(Character_Mine_Artifact, pk=pk)
                instance.delete()

                context["data"] = "deleted_gear"
                return JsonResponse(context)
            
            elif function == 'equip_targa_artifact_instance':
                pk = data['targa_artifact_instance']
                instance = get_object_or_404(Character_Targa_Artifact,pk = pk)
                instance.equiped = True

                instance.save()

                context['equiped'] = 'a'
                return JsonResponse(context)
        
            elif function == "delete_targa_artifact":
                pk = data['targa_artifact_instance']
                instance = get_object_or_404(Character_Targa_Artifact, pk=pk)
                instance.delete()

                context["data"] = "deleted_gear"
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
    
class Create_Character_Gear(CreateView):
    model = Character_Gear
    form_class = Add_Character_Gear
    template_name = "new_character_gear.html"

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
    
class Create_Character_Mine_Artifact(CreateView):
    model = Character_Mine_Artifact
    form_class = Add_Character_Mine_Artifact
    template_name = "new_character_mine_artifact.html"

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
    
class Create_Character_Targa_Artifact(CreateView):

    model = Character_Targa_Artifact
    form_class = Add_Character_Targa_Artifact
    template_name = "new_character_targa_artifact.html"

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
