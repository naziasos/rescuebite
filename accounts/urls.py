from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),

    path('profiles/',views.profile_list,name='profile_list'),

    path('notifications/',views.notification_list,name='notification_list'),
path('create-profile/',
     views.create_profile,
     name='create_profile'),

path('update-profile/<int:id>/',
     views.update_profile,
     name='update_profile'),

path('delete-profile/<int:id>/',
     views.delete_profile,
     name='delete_profile'),
path('create-notification/',
     views.create_notification,
     name='create_notification'),

path('update-notification/<int:id>/',
     views.update_notification,
     name='update_notification'),
path('login/',
     views.login_page,
     name='login'),

path('register/',
     views.register_page,
     name='register'),

path('dashboard/',
     views.dashboard,
     name='dashboard'),

path('logout/',
     views.logout_page,
     name='logout'),
]