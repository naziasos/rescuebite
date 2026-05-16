from django.urls import path

from . import views

urlpatterns = [
    path('deliveries/',
         views.delivery_list,
         name='delivery_list'),
path('create-delivery/',
     views.create_delivery,
     name='create_delivery'),

path('update-delivery/<int:id>/',
     views.update_delivery,
     name='update_delivery'),
]