from django.urls import path

from .views import All_Characters,Character_View

urlpatterns = [
    path("<int:pk>", Character_View.as_view(), name="character_detail"),
    path("",All_Characters.as_view(),name = 'All_Characters'),
]