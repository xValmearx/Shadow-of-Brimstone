from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationFrom,
    CustomUserChangeForm,
)

from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        'username',
        'email',
        'is_staff',
        'age',

    ]

admin.site.register(CustomUser, CustomUserAdmin)
