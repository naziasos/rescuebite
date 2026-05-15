from django.shortcuts import render
from .models import Delivery

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request,
                  'delivery/delivery_list.html',
                  {'deliveries': deliveries})
