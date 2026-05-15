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
]