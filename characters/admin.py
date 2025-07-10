from django.contrib import admin

from .models import Character, Passive_Buff, Per_Turn, Per_Fight, Per_Adventure,Side_Bag, Character_Gear, Character_Mine_Artifact

admin.site.register(Character)
admin.site.register(Passive_Buff)
admin.site.register(Per_Turn)
admin.site.register(Per_Fight)
admin.site.register(Per_Adventure)
admin.site.register(Side_Bag)
admin.site.register(Character_Gear)
admin.site.register(Character_Mine_Artifact)

# Register your models here.
