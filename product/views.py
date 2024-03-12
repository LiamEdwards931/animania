from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def index(request):
    messages_to_render = messages.get_messages(request)
    return render(request, 'index.html',{'messages': messages_to_render})

def amendProducts(request):
    return render(request, 'amendproducts.html')