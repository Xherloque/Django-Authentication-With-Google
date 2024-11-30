from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home View
def home(request):
    return render(request, 'users/home.html')

# Register View
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'users/register.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        email_or_username = request.POST['email_or_username']
        if '@' in email_or_username:  # Assuming input is email
            try:
                user = User.objects.get(email=email_or_username)
                return redirect('login_password', username=user.username)
            except User.DoesNotExist:
                messages.error(request, "No account found with this email")
        else:  # Assuming input is username
            return redirect('login_password', username=email_or_username)
    return render(request, 'users/login.html')

# Login Password View
def login_password(request, username):
    if request.method == 'POST':
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'users/login_password.html', {'username': username})

# Profile View
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')
