from django.db import models
from django.conf import settings
from django.urls import reverse

from equipment.models import Token, Gear, Mine_Artifact, Targa_Artifact


class Character(models.Model):

    # define the user of the character model
    character_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="marshal_character",
    )

    class_options = (
        ("Marshal", "Marshal"),
        ("Rancher", "Rancher"),
        ("LawMan","LawMan"),
        ("PianoPlayer","PianoPlayer"),
        ("IndianScout","IndianScout"),
        ("Bandido","Bandido"),
        ("Preacher","Preacher"),
        ("GunSlinger","GunSlinger"),
    )

    character_class = models.CharField(choices=class_options, default="Marshal")

    # user gets to name the character
    character_name = models.CharField(max_length=25,blank=False)

    character_init = models.BooleanField(default= False)

    # skills
    agility = models.IntegerField(default=0)
    cunning = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    # combat skills
    initiative = models.IntegerField(default=0)
    range_to_hit = models.IntegerField(default=0)
    melee_to_hit = models.IntegerField(default=0)
    combat = models.IntegerField(default=0)
    
# health and sanity
    health = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    sanity = models.IntegerField(default=0)
    willpower = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        if self.character_init == False:
            if self.character_class == 'Marshal':

                # stats
                self.agility = 3
                self.cunning = 4
                self.spirit = 2
                self.strength = 2
                self.lore = 1
                self.luck = 3
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 4
                self.range_to_hit = 4
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 10
                self.defence = 3
                self.sanity = 10
                self.willpower = 4

            elif self.character_class == 'Rancher':
                # stats
                self.agility = 2
                self.cunning = 2
                self.spirit = 3
                self.strength = 3
                self.lore = 4
                self.luck = 1
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 3
                self.range_to_hit = 4
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 14
                self.defence = 4
                self.sanity = 10
                self.willpower = 4

            elif self.character_class == 'LawMan':
                # stats
                self.agility = 2
                self.cunning = 4
                self.spirit = 1
                self.strength = 3
                self.lore = 2
                self.luck = 3
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 4
                self.range_to_hit = 4
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 12
                self.defence = 4
                self.sanity = 12
                self.willpower = 4

            elif self.character_class == 'PianoPlayer':
                # stats
                self.agility = 4
                self.cunning = 3
                self.spirit = 3
                self.strength = 1
                self.lore = 2
                self.luck = 3
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 5
                self.range_to_hit = 4
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 8
                self.defence = 3
                self.sanity = 14
                self.willpower = 4

            elif self.character_class == 'IndianScout':
                # stats
                self.agility = 3
                self.cunning = 2
                self.spirit = 3
                self.strength = 2
                self.lore = 3
                self.luck = 2
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 5
                self.range_to_hit = 4
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 10
                self.defence = 3
                self.sanity = 10
                self.willpower = 4

            elif self.character_class == 'Bandido':
                # stats
                self.agility = 2
                self.cunning = 1
                self.spirit = 3
                self.strength = 4
                self.lore = 3
                self.luck = 2
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 3
                self.range_to_hit = 5
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 16
                self.defence = 4
                self.sanity = 8
                self.willpower = 5

            if self.character_class == 'Preacher':
                # stats
                self.agility = 1
                self.cunning = 2
                self.spirit = 4
                self.strength = 3
                self.lore = 3
                self.luck = 2
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 2
                self.range_to_hit = 5
                self.melee_to_hit = 4
                self.combat = 2

                # health and sanity
                self.health = 12
                self.defence = 5
                self.sanity = 10
                self.willpower = 3

            if self.character_class == 'GunSlinger':
                # stats
                self.agility = 3
                self.cunning = 3
                self.spirit = 2
                self.strength = 2
                self.lore = 2
                self.luck = 4
                
                self.weight = 5 + self.strength

                # combat stats
                self.initiative = 6
                self.range_to_hit = 3
                self.melee_to_hit = 5
                self.combat = 1

                # health and sanity
                self.health = 10
                self.defence = 5
                self.sanity = 12
                self.willpower = 4

            self.character_init = True
        super(Character,self).save(*args, **kwargs)
  
    current_weight = models.IntegerField(default=0)

    current_health = models.IntegerField(default = 0)
    current_sanity = models.IntegerField(default= 0 )

    max_grit = models.IntegerField(default=2)
    current_grit = models.IntegerField(default=2)

    corruption = models.IntegerField(default=5)
    current_corruption = models.IntegerField(default=0)

    class_card = models.IntegerField(default=1)

    gold = models.IntegerField(default=0)
    dark_stone = models.IntegerField(default=0)

    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)


    def __str__(self):
        return self.character_name
    
    def get_absolute_url(self):
        return reverse("character_detail",kwargs={'pk': self.pk})

# character buffs    
class Passive_Buff(models.Model):

    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='passive_buffs')
    
    name = models.CharField(blank= False,default= "buff name here")

    text = models.TextField(blank= False, default= "text here")

    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.name}'
        except:
            return self.name
        
class Per_Turn(models.Model):
    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='per_turn')
    
    name = models.CharField(blank= False,default= "buff name here")

    text = models.TextField(blank= False, default= "text here")

    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.name}'
        except:
            return self.name
        
class Per_Fight(models.Model):
    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='per_fight')
    
    name = models.CharField(blank= False,default= "buff name here")

    text = models.TextField(blank= False, default= "text here")

    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.name}'
        except:
            return self.name

class Per_Adventure(models.Model):
    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='per_adventure')
    
    name = models.CharField(blank= False,default= "buff name here")

    text = models.TextField(blank= False, default= "text here")

    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.name}'
        except:
            return self.name
    
# gear and equipment
class Side_Bag(models.Model):

    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='side_bag')
    
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
          related_name='character_token',
          default= 1)
    
    def get_absolute_url(self):
        return self.assigned_to_character.get_absolute_url()
    
    
    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.token}'
        except:
            return "Side Bag"
    
class Character_Gear(models.Model):
    
    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='equiped_gear')
    
    gear = models.ForeignKey(
        Gear,
        on_delete=models.CASCADE,
          related_name='character_gear',
          default= 1)
    
    equiped = models.BooleanField(default= False)
    
    def get_absolute_url(self):
        return self.assigned_to_character.get_absolute_url()
    
    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.gear}'
        except:
            return "Character Gear"

class Character_Mine_Artifact(models.Model):
    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='equiped_mine_artifact')
    
    mine_artifact = models.ForeignKey(
        Mine_Artifact,
        on_delete=models.CASCADE,
          related_name='character_mine_artifact',
          default= 1)
    
    equiped = models.BooleanField(default= False)
    
    def get_absolute_url(self):
        return self.assigned_to_character.get_absolute_url()
    
    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.mine_artifact}'
        except:
            return "Mine Artifact"

class Character_Targa_Artifact(models.Model):
    assigned_to_character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
          related_name='equiped_targa_artifact')
    
    targa_artifact = models.ForeignKey(
        Targa_Artifact,
        on_delete=models.CASCADE,
          related_name='character_targa_artifact',
          default= 1)
    
    equiped = models.BooleanField(default= False)
    
    def get_absolute_url(self):
        return self.assigned_to_character.get_absolute_url()
    
    def __str__(self):
        try:
            return f'{self.assigned_to_character} {self.targa_artifact}'
        except:
            return "Targa Artifact"