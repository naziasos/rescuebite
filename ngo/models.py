from django.db import models

from django.contrib.auth.models import User


class NGO(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    ngo_name = models.CharField(max_length=100)

    def __str__(self):

        return self.ngo_name


class Volunteer(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    ngo = models.ForeignKey(NGO,
                            on_delete=models.CASCADE)

    vehicle = models.CharField(max_length=100)

    image = models.ImageField(upload_to='volunteer_images/', null=True, blank=True)

    def __str__(self):

        return self.user.username
