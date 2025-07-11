from django.db import models

# Create your models here.

class Token(models.Model):

    name = models.CharField(default= "Token")
    description = models.TextField(default= "Discard to ")
    
    def __str__(self):
        return self.name

class Gear(models.Model):

    name = models.CharField(default="Gear Name")
    description = models.TextField(default="Dose stuff")

    buff_options = (
        ("none","none"),
        ('passive','passive'),
        ('turn','turn'),
        ('fight','fight'),
        ('adventure','adventure'),
    )

    buff_type = models.CharField(choices= buff_options, default="none")

    weight = models.IntegerField(default=1)

    value = models.CharField(default=0)

    dark_stone = models.IntegerField(default=0)

    agility_buff = models.IntegerField(default=0)
    cunning_buff = models.IntegerField(default=0)
    spirit_buff = models.IntegerField(default=0)
    strength_buff = models.IntegerField(default=0)
    lore_buff = models.IntegerField(default=0)
    luck_buff = models.IntegerField(default=0)
    initiative_buff = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Mine_Artifact(models.Model):
    name = models.CharField(default="Gear Name")
    description = models.TextField(default="Dose stuff")

    buff_options = (
        ("none","none"),
        ('passive','passive'),
        ('turn','turn'),
        ('fight','fight'),
        ('adventure','adventure'),
    )

    buff_type = models.CharField(choices= buff_options, default="none")

    weight = models.IntegerField(default=1)

    value = models.CharField(default=0)

    dark_stone = models.IntegerField(default=0)

    agility_buff = models.IntegerField(default=0)
    cunning_buff = models.IntegerField(default=0)
    spirit_buff = models.IntegerField(default=0)
    strength_buff = models.IntegerField(default=0)
    lore_buff = models.IntegerField(default=0)
    luck_buff = models.IntegerField(default=0)
    initiative_buff = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Targa_Artifact(models.Model):
    name = models.CharField(default="Gear Name")
    description = models.TextField(default="Dose stuff")

    buff_options = (
        ("none","none"),
        ('passive','passive'),
        ('turn','turn'),
        ('fight','fight'),
        ('adventure','adventure'),
    )

    buff_type = models.CharField(choices= buff_options, default="none")

    weight = models.IntegerField(default=1)

    value = models.CharField(default=0)

    dark_stone = models.IntegerField(default=0)

    agility_buff = models.IntegerField(default=0)
    cunning_buff = models.IntegerField(default=0)
    spirit_buff = models.IntegerField(default=0)
    strength_buff = models.IntegerField(default=0)
    lore_buff = models.IntegerField(default=0)
    luck_buff = models.IntegerField(default=0)
    initiative_buff = models.IntegerField(default=0)
    grit_buff = models.IntegerField(default=0)

    def __str__(self):
        return self.name
