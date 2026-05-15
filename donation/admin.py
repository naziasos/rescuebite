from django.contrib import admin

from .models import FoodItem,Claim,DonationHistory


admin.site.register(FoodItem)

admin.site.register(Claim)

admin.site.register(DonationHistory)
