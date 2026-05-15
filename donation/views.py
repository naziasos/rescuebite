from django.shortcuts import render

from .models import FoodItem, Claim, DonationHistory


# FOOD LIST

def food_list(request):

    foods = FoodItem.objects.all()

    return render(request,
                  'donation/food_list.html',
                  {'foods': foods})

# CLAIM LIST
def claim_list(request):

    claims = Claim.objects.all()

    return render(request,
                  'donation/claim_list.html',
                  {'claims': claims})

# DONATION HISTORY LIST
def donation_history_list(request):

    history = DonationHistory.objects.all()

    return render(request,
                  'donation/donation_history_list.html',
                  {'history': history})