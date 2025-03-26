from django.contrib.messages import success
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignupForm
from django.views.generic import FormView
from django.urls import reverse_lazy
# Create your views here.
def index_view(request):
    return HttpResponse("로그인 완료")

class login_view(FormView):
    template_name = "users/users.html"
    form_class = LoginForm
    success_url = reverse_lazy("users:index")
    def form_valid(self, form):
        user_email = form.cleaned_data.get("user_email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect("users:login_view")

class signup_view(FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:login")
    def form_valid(self, form):
        form.save()
        user_email = form.cleaned_data.get("user_email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    # if request.method == "POST":
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("users:login_view")
    # else:
    #     form = SignupForm()
    #
    # return render(request, "users/signup.html", {"form":form})
