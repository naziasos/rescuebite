from django.shortcuts import render,redirect

from .models import Delivery

from .forms import DeliveryForm

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request,
                  'delivery/delivery_list.html',
                  {'deliveries': deliveries})

def create_delivery(request):

    if request.method == 'POST':

        form = DeliveryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/delivery/deliveries/')

    else:

        form = DeliveryForm()

    return render(request,
                  'delivery/forms.html',
                  {'form': form})

def update_delivery(request,id):

    delivery = Delivery.objects.get(pk=id)

    if request.method == 'POST':

        form = DeliveryForm(request.POST,
                            instance=delivery)

        if form.is_valid():

            form.save()

            return redirect('/delivery/deliveries/')

    else:

        form = DeliveryForm(instance=delivery)

    return render(request,
                  'delivery/forms.html',
                  {'form': form})
