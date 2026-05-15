from django.urls import path

from . import views

urlpatterns = [

    path('ngos/',
         views.ngo_list,
         name='ngo_list'),

    path('volunteers/',
         views.volunteer_list,
         name='volunteer_list'),
]