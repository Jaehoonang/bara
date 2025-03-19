from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm

# Create your views here.
def index(request):
    return HttpResponse("users views")

def login(request):
    if request.user.is_authenticated:
        return redirect("users:index")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users:index")
    else:
        form = LoginForm()

    return render(request, "users/users.html", {"form": form})

def logout(request):
    logout(request)
    return redirect("users:index")