from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReviewPostForm, ItemPostForm
from .models import Review, Item
from django.urls import reverse

# Create your views here.
def review(request):
    return HttpResponse("review List")

def item(request):
    return HttpResponse("item List")


def review_post(request):
    if request.method == "POST":
        form = ReviewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse('reviews:review'))
    else:
        form = ReviewPostForm()

    return render(request, 'reviews/review_form.html', {'form':form})


def item_post(request):
    if request.method == "POST":
        form = ItemPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse('reviews:item'))
        else:
            form = ItemPostForm()

    return render(request, 'reviews/item_form.html', {'form':form})


