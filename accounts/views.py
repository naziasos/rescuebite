from django.shortcuts import render
from .models import Profile, Notification

# homepage
def home(request):
    return render(request,
                  'accounts/home.html')


# PROFILE LIST
def profile_list(request):
    profiles = Profile.objects.all()

    return render(request,
                  'accounts/profile_list.html',
                  {'profiles': profiles})


# NOTIFICATION LIST
def notification_list(request):
    notifications = Notification.objects.all()

    return render(request,
                  'accounts/notification_list.html',
                  {'notifications': notifications})

