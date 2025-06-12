from django.apps import apps
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView
# Create your views here.

from .models import Character

class All_Characters(ListView):
    model = Character


    template_name = "All_Characters.html"