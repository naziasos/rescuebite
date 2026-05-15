from django.db import models

from donation.models import Claim

from ngo.models import Volunteer


class Delivery(models.Model):

    claim = models.ForeignKey(Claim,
                              on_delete=models.CASCADE)

    volunteer = models.ForeignKey(Volunteer,
                                  on_delete=models.CASCADE)

    status = models.CharField(max_length=50,
                              default='Assigned')

    def __str__(self):

        return self.status