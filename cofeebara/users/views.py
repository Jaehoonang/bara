from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, SignupForm

# Create your views here.
def index_view(request):
    return HttpResponse("로그인 완료")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("reviews:review_list")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users:index")
    else:
        form = LoginForm()
    print(request.user)
    return render(request, "users/users.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("users:login_view")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("users:login_view")
    else:
        form = SignupForm()

    return render(request, "users/signup.html", {"form":form})