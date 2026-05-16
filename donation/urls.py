from django.urls import path
from . import views

urlpatterns = [
    path('foods/',
         views.food_list,
         name='food_list'),
    path('claims/',
         views.claim_list,
         name='claim_list'),
    path('history/',
         views.donation_history_list,
         name='donation_history_list'),
path('create-food/',
     views.create_food,
     name='create_food'),

path('update-food/<int:id>/',
     views.update_food,
     name='update_food'),

path('delete-food/<int:id>/',
     views.delete_food,
     name='delete_food'),

path('create-claim/',
     views.create_claim,
     name='create_claim'),

path('update-claim/<int:id>/',
     views.update_claim,
     name='update_claim'),
]