from django.urls import path

from . import views

urlpatterns = [

    path('ngos/',
         views.ngo_list,
         name='ngo_list'),

    path('volunteers/',
         views.volunteer_list,
         name='volunteer_list'),
path('create-ngo/',
     views.create_ngo,
     name='create_ngo'),

path('update-ngo/<int:id>/',
     views.update_ngo,
     name='update_ngo'),

path('create-volunteer/',
     views.create_volunteer,
     name='create_volunteer'),

path('update-volunteer/<int:id>/',
     views.update_volunteer,
     name='update_volunteer'),
]