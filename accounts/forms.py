from django import forms

from .models import Profile, Notification


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = '__all__'

class NotificationForm(forms.ModelForm):

    class Meta:

        model = Notification

        fields = '__all__'