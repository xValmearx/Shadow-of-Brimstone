from django.urls import path

from .views import All_Characters,Character_View, Create_Side_Bag_Token, Create_Character_Gear

urlpatterns = [
    path("Add_Token/<int:pk>/",Create_Side_Bag_Token.as_view(),name = "add_token"),
    path("Add_Gear/<int:pk>/",Create_Character_Gear.as_view(),name = "add_gear"),
    path("<int:pk>/", Character_View.as_view(), name="character_detail"),
    path("",All_Characters.as_view(),name = 'All_Characters'),
]