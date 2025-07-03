from django.contrib import admin

# Register your models here.

from .models import Token, Gear

admin.site.register(Token)
admin.site.register(Gear)