from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import NGO, Volunteer

from .forms import NGOForm, VolunteerForm


# NGO LIST

def ngo_list(request):

    ngos = NGO.objects.all()

    return render(request,
                  'ngo/ngo_list.html',
                  {'ngos': ngos})


# VOLUNTEER LIST

def volunteer_list(request):

    volunteers = Volunteer.objects.all()

    return render(request,
                  'ngo/volunteer_list.html',
                  {'volunteers': volunteers})

@login_required
def create_ngo(request):

    if request.method == 'POST':

        form = NGOForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/ngo/ngos/')

    else:

        form = NGOForm()

    return render(request,
                  'ngo/forms.html',
                  {'form': form})
@login_required
def update_ngo(request,id):

    ngo = NGO.objects.get(pk=id)

    if request.method == 'POST':

        form = NGOForm(request.POST,
                       instance=ngo)

        if form.is_valid():

            form.save()

            return redirect('/ngo/ngos/')

    else:

        form = NGOForm(instance=ngo)

    return render(request,
                  'ngo/forms.html',
                  {'form': form})

@login_required

def create_volunteer(request):

    if request.method == 'POST':

        form = VolunteerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/ngo/volunteers/')

    else:
        form = VolunteerForm()

    return render(request, 'ngo/forms.html', {'form': form})


@login_required
@login_required
def update_volunteer(request, id):

    volunteer = Volunteer.objects.get(pk=id)

    if request.method == 'POST':

        form = VolunteerForm(request.POST, request.FILES, instance=volunteer)

        if form.is_valid():
            form.save()
            return redirect('/ngo/volunteers/')

    else:
        form = VolunteerForm(instance=volunteer)

    return render(request, 'ngo/forms.html', {'form': form})
