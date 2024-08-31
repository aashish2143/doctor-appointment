from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

def handle_login(request, email, password):
    user = authenticate(request, email=email, password=password)
    if user is not None:
        if user.is_staff | user.is_superuser:
            login(request, user)
            username = user.username
            messages.success(request, f"Welcome, {username}!")
            return redirect('dashboard:home')
        else:
            messages.error(request, "You are not authorized to access this page.")
            return None
    else:
        messages.error(request, "Invalid email or password! Please try again.")
        return None