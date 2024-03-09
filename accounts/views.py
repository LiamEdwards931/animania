from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.shortcuts import render,redirect
# Create your views here.

@receiver(user_logged_in)
# view to display a log in message 
def show_login_message(sender, user, request, **kwargs):
    messages.info(request, f"Welcome to Animania {user.username}")

@receiver(user_logged_out)
# view to display a log out message
def show_logout_message(sender, user, request, **kwargs):
    if user is not None:
        messages.info(request, f"Goodbye {user.username}, We hope you enjoyed your visit!")

def profile(request):
    # View for the user profile page
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)
