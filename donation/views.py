from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .forms import FoodItemForm, ClaimForm

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

@login_required
def create_food(request):

    if request.method == 'POST':

        form = FoodItemForm(request.POST, request.FILES)  # 🔥 FIXED

        if form.is_valid():

            form.save()

            return redirect('/donation/foods/')

    else:

        form = FoodItemForm()

    return render(request,
                  'donation/forms.html',
                  {'form': form})
@login_required
def update_food(request,id):

    food = FoodItem.objects.get(pk=id)

    if request.method == 'POST':

        form = FoodItemForm(request.POST,
                            instance=food)

        if form.is_valid():

            form.save()

            return redirect('/donation/foods/')

    else:

        form = FoodItemForm(instance=food)

    return render(request,
                  'donation/forms.html',
                  {'form': form})

@login_required
def delete_food(request,id):

    food = FoodItem.objects.get(pk=id)

    food.delete()

    return redirect('/donation/foods/')

def create_claim(request):

    if request.method == 'POST':

        form = ClaimForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/donation/claims/')

    else:

        form = ClaimForm()

    return render(request,
                  'donation/claim_form.html',
                  {'form': form})

def update_claim(request,id):

    claim = Claim.objects.get(pk=id)

    if request.method == 'POST':

        form = ClaimForm(request.POST,
                         instance=claim)

        if form.is_valid():

            form.save()

            return redirect('/donation/claims/')

    else:

        form = ClaimForm(instance=claim)

    return render(request,
                  'donation/claim_form.html',
                  {'form': form})