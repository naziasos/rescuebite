from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    USER_TYPES = (
        ('person', 'Person'),
        ('ngo', 'NGO'),
        ('restaurant', 'Restaurant'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='person'
    )

    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Notification(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    def __str__(self):

        return self.message