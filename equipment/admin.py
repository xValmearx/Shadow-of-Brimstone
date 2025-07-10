from django.contrib import admin

# Register your models here.

from .models import Token, Gear, Mine_Artifact

admin.site.register(Token)
admin.site.register(Gear)
admin.site.register(Mine_Artifact)