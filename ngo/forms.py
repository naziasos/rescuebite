from django import forms

from .models import NGO, Volunteer


class NGOForm(forms.ModelForm):

    class Meta:

        model = NGO

        fields = '__all__'


class VolunteerForm(forms.ModelForm):

    class Meta:

        model = Volunteer

        fields = '__all__'