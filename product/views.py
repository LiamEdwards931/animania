from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

