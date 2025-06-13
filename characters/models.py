from django.db import models
from django.conf import settings
from django.urls import reverse


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
        ("PianoPlayer/SaloonGirl","PianoPlayer/SaloonGirl"),
        ("IndianScout","IndianScout"),
        ("Bandido","Bandido"),
        ("Preacher","Preacher"),
        ("GunSlinger","GunSlinger"),

    )

    character_class = models.CharField(choices=class_options, default="Marshal")

    # user gets to name the character
    character_name = models.CharField(max_length=25,blank=False)

    @property
    def agility(self):
        if self.character_class == "Marshal":
            return 3
        if self.character_class == "Rancher":
            return 2
        if self.character_class == "LawMan":
            return 2
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 4
        if self.character_class == "IndianScout":
            return 3
        if self.character_class == "Bandido":
            return 2
        if self.character_class == "Preacher":
            return 1
        if self.character_class == "GunSlinger":
            return 3
    def cunning(self):
        if self.character_class == "Marshal":
            return 4
        if self.character_class == "Rancher":
            return 2
        if self.character_class == "LawMan":
            return 4
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 3
        if self.character_class == "IndianScout":
            return 2
        if self.character_class == "Bandido":
            return 1
        if self.character_class == "Preacher":
            return 2
        if self.character_class == "GunSlinger":
            return 3
    def spirit(self):
        if self.character_class == "Marshal":
            return 2
        if self.character_class == "Rancher":
            return 3
        if self.character_class == "LawMan":
            return 1
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 3
        if self.character_class == "IndianScout":
            return 3
        if self.character_class == "Bandido":
            return 3
        if self.character_class == "Preacher":
            return 4
        if self.character_class == "GunSlinger":
            return 2
    def strength(self):
        if self.character_class == "Marshal":
            return 2
        if self.character_class == "Rancher":
            return 3
        if self.character_class == "LawMan":
            return 3
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 1
        if self.character_class == "IndianScout":
            return 2
        if self.character_class == "Bandido":
            return 4
        if self.character_class == "Preacher":
            return 3
        if self.character_class == "GunSlinger":
            return 2
    def lore(self):
        if self.character_class == "Marshal":
            return 1
        if self.character_class == "Rancher":
            return 4
        if self.character_class == "LawMan":
            return 2
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 2
        if self.character_class == "IndianScout":
            return 3
        if self.character_class == "Bandido":
            return 3
        if self.character_class == "Preacher":
            return 3
        if self.character_class == "GunSlinger":
            return 2
    def luck(self):
        if self.character_class == "Marshal":
            return 3
        if self.character_class == "Rancher":
            return 1
        if self.character_class == "LawMan":
            return 3
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 3
        if self.character_class == "IndianScout":
            return 2
        if self.character_class == "Bandido":
            return 2
        if self.character_class == "Preacher":
            return 2
        if self.character_class == "GunSlinger":
          
            return 4
    def initiative(self):
        if self.character_class == "Marshal":
            return 4
        if self.character_class == "Rancher":
            return 3
        if self.character_class == "LawMan":
            return 4
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 5
        if self.character_class == "IndianScout":
            return 5
        if self.character_class == "Bandido":
            return 3
        if self.character_class == "Preacher":
            return 2
        if self.character_class == "GunSlinger":
            return 6
    def range_to_hit(self):
        if self.character_class == "Marshal":
            return 4
        if self.character_class == "Rancher":
            return 4
        if self.character_class == "LawMan":
            return 4
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 4
        if self.character_class == "IndianScout":
            return 4
        if self.character_class == "Bandido":
            return 5
        if self.character_class == "Preacher":
            return 5
        if self.character_class == "GunSlinger":
            return 3
    def melee_to_hit(self):
        if self.character_class == "Marshal":
            return 4
        if self.character_class == "Rancher":
            return 4
        if self.character_class == "LawMan":
            return 4
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 4
        if self.character_class == "IndianScout":
            return 4
        if self.character_class == "Bandido":
            return 4
        if self.character_class == "Preacher":
            return 4
        if self.character_class == "GunSlinger":
            return 5
        
    def combat(self):
        if self.character_class == "GunSlinger":
            return 1
        else:
            return 2
    def health(self):
        if self.character_class == "Marshal":
            return 10
        if self.character_class == "Rancher":
            return 14
        if self.character_class == "LawMan":
            return 12
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 8
        if self.character_class == "IndianScout":
            return 10
        if self.character_class == "Bandido":
            return 16
        if self.character_class == "Preacher":
            return 12
        if self.character_class == "GunSlinger":
            return 10
    def defence(self):
        if self.character_class == "Marshal":
            return 3
        if self.character_class == "Rancher":
            return 4
        if self.character_class == "LawMan":
            return 4
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 3
        if self.character_class == "IndianScout":
            return 4
        if self.character_class == "Bandido":
            return 4
        if self.character_class == "Preacher":
            return 5
        if self.character_class == "GunSlinger":
            return 5
    def sanity(self):
        if self.character_class == "Marshal":
            return 10
        if self.character_class == "Rancher":
            return 10
        if self.character_class == "LawMan":
            return 12
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 14
        if self.character_class == "IndianScout":
            return 10
        if self.character_class == "Bandido":
            return 8
        if self.character_class == "Preacher":
            return 10
        if self.character_class == "GunSlinger":
            return 12
    def willpower(self):
        if self.character_class == "Marshal":
            return 4
        if self.character_class == "Rancher":
            return 4
        if self.character_class == "LawMan":
            return 4
        if self.character_class == "PianoPlayer/SaloonGirl":
            return 4
        if self.character_class == "IndianScout":
            return 4
        if self.character_class == "Bandido":
            return 5
        if self.character_class == "Preacher":
            return 3
        if self.character_class == "GunSlinger":
            return 4
    def weight(self):
        return 5 + self.strength()
    
    max_grit = models.IntegerField(default=2)
    def __str__(self):
        return self.character_name
    
    def get_absolute_url(self):
        return reverse("character_detail",kwargs={'pk': self.pk})
    
