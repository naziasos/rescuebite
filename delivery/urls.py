from django.urls import path

from . import views

urlpatterns = [
    path('deliveries/',
         views.delivery_list,
         name='delivery_list'),
]