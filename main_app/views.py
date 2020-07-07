from django.shortcuts import render, redirect
from .models import Subscriber
from .forms import Subscriber_Form
from django.http import HttpResponse
from django.db.models.functions import Lower

# Create your views here.

def home(request):
    return render(request, 'home.html')

def adminpage(request):
    return render(request, 'adminpage.html')

# index & create
def subscribe(request):
    error_message = ''
    if request.method == 'POST':
        subscriber_form = Subscriber_Form(request.POST)
        if subscriber_form.is_valid():
            new_subscriber = subscriber_form.save(commit=False)
            new_subscriber.save()
            subscriber_form = Subscriber_Form()
            return render(request, 'home.html', { 'subscribed': True, 'subscriber_form': subscriber_form })
        else:
            error_message = 'Error - All fields must be completed. Valid e-mail address required.'
    else:
        subscriber_form = Subscriber_Form()
    subscribers = Subscriber.objects.all()
    context = {'subscribers':subscribers, 'subscriber_form':subscriber_form, 'error_message':error_message}
    return render(request, 'home.html', context)
    
# show 

def show_subscribers(request):
    subscribers = Subscriber.objects.all().order_by(Lower('last_name'))
    context = {'subscribers':subscribers}
    return render(request, 'adminpage.html', context)
