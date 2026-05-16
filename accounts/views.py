from django.shortcuts import render,redirect

from .models import Profile, Notification

from .forms import ProfileForm, NotificationForm

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

def create_profile(request):

    if request.method == 'POST':

        form = ProfileForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/profiles/')

    else:

        form = ProfileForm()

    return render(request,
                  'accounts/forms.html',
                  {'form': form})

def update_profile(request,id):

    profile = Profile.objects.get(pk=id)

    if request.method == 'POST':

        form = ProfileForm(request.POST,
                           instance=profile)

        if form.is_valid():

            form.save()

            return redirect('/profiles/')

    else:

        form = ProfileForm(instance=profile)

    return render(request,
                  'accounts/forms.html',
                  {'form': form})

def delete_profile(request,id):

    profile = Profile.objects.get(pk=id)

    profile.delete()

    return redirect('/profiles/')

def create_notification(request):

    if request.method == 'POST':

        form = NotificationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/notifications/')

    else:

        form = NotificationForm()

    return render(request,
                  'accounts/notification_form.html',
                  {'form': form})

def update_notification(request,id):

    notification = Notification.objects.get(pk=id)

    if request.method == 'POST':

        form = NotificationForm(request.POST,
                                instance=notification)

        if form.is_valid():

            form.save()

            return redirect('/notifications/')

    else:

        form = NotificationForm(instance=notification)

    return render(request,
                  'accounts/notification_form.html',
                  {'form': form})