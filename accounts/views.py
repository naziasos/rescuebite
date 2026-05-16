from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

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

def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,
            username=username,
            password=password

        )

        if user is not None:

            login(request,user)

            return redirect('/dashboard/')

        else:

            return render(request,
                          'accounts/login.html',
                          {'error':'Invalid Username or Password'})

    return render(request,
                  'accounts/login.html')

def register_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():

            return render(request,
                          'accounts/register.html',
                          {'error':'Username already exists'})

        user = User.objects.create_user(

            username=username,
            password=password,
            email=email

        )

        user.save()

        return redirect('/login/')

    return render(request,
                  'accounts/register.html')

def dashboard(request):

    return render(request,
                  'accounts/dashboard.html')
def logout_page(request):

    logout(request)

    return redirect('/login/')