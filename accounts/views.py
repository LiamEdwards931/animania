from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
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

# Creates a custom user creation
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Your account has been created {user.username}')
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
