from django.shortcuts import render
from .models import NGO, Volunteer


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