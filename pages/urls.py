from django.urls import path

from .views import All_Characters

urlpatterns = [
    path("",All_Characters.as_view(),name = 'All_Characters'),
]