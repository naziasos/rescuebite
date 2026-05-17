from django.db import models
from accounts.models import Notification

from django.contrib.auth.models import User


class FoodItem(models.Model):
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default='Available')

    expiry_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            Notification.objects.create(
                user=self.restaurant,
                message=f"🍱 New food added: {self.food_name}"
            )

    def __str__(self):
        return self.food_name


class Claim(models.Model):

    food = models.ForeignKey(FoodItem,
                             on_delete=models.CASCADE)

    ngo = models.ForeignKey(User,
                            on_delete=models.CASCADE)

    status = models.CharField(max_length=50,
                              default='Pending')

    def __str__(self):

        return self.food.food_name


class DonationHistory(models.Model):

    food = models.ForeignKey(FoodItem,
                             on_delete=models.CASCADE)

    restaurant = models.ForeignKey(User,
                                   related_name='restaurant_history',
                                   on_delete=models.CASCADE)

    ngo = models.ForeignKey(User,
                            related_name='ngo_history',
                            on_delete=models.CASCADE)

    def __str__(self):

        return self.food.food_name