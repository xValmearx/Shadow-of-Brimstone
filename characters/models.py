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
        ("Rager", "Ranger"),
    )

    character_class = models.CharField(choices=class_options, default="Marshal")

    # user gets to name the character
    character_name = models.CharField(max_length=25,blank=False)

    agility = models.IntegerField(default=3)
    cunning = models.IntegerField(default=4)
    spirit = models.IntegerField(default=2)
    strength = models.IntegerField(default=2)
    lore = models.IntegerField(default=1)
    luck = models.IntegerField(default=3)

    initiative = models.IntegerField(default=4)

    range_to_hit = models.IntegerField(default=4)
    melee_to_hit = models.IntegerField(default=4)
    combat = models.IntegerField(default=2)

    max_grit = models.IntegerField(default=2)

    health = models.IntegerField(default=10)
    defence = models.IntegerField(default=3)

    sanity = models.IntegerField(default=10)
    willpower = models.IntegerField(default=4)

    @property
    def weight(self):
        return 5 + self.strength

    def __str__(self):
        return self.character_name
    
    def get_absolute_url(self):

        if self.character_class == 'Marshal':
            return reverse("marshall_detail",kwargs={'pk': self.pk})
        
        elif self.character_class == 'Ranger':
            return reverse("ranger_detail",kwargs={'pk': self.pk})
    
