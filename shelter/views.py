from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from shelter.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("Hello, We Are Well-known & A Reputed Pharmacy Supplier Since 2021")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')  
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details Are Submitted We Will Contact You Soon') 
    return render(request, 'contact.html')
    #return HttpResponse("Please Do Not Disturb")