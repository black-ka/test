from ast import Name
import email
from multiprocessing import context
from unicodedata import name
from webbrowser import get
from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Harsh is great",
        "variable2":"im is great"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('name')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been sent!')
    return render(request, 'contact.html')