from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check if user exist in the system with above credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("project_list")
        else:
            messages.error(request, "Invalid username or password")
    return render(request,'accounts/login.html')

# if a user is not logged in our login_required decorator will redirect back to the login page
# else we allow user to see the homepage
@login_required
def home_view(request):
    return render(request,'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect("login")








