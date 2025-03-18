from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReviewPostForm
from .models import Review, Item
from django.urls import reverse

# Create your views here.
def review(request):
    return HttpResponse("review List")

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