from django import forms

from .models import FoodItem, Claim

class FoodItemForm(forms.ModelForm):

    class Meta:

        model = FoodItem

        fields = '__all__'

class ClaimForm(forms.ModelForm):

    class Meta:

        model = Claim

        fields = '__all__'