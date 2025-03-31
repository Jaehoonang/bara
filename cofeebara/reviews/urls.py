from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.review, name="review_list"),
    path("post/", views.review_post, name="review_post"),
    path("item/", views.item_post, name="item_post"),
]