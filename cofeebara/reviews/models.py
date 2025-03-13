import uuid

from django.db import models
from django.db.models import UUIDField, ForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Rating_star(models.IntegerChoices):
    ONE = 1, '★☆☆☆☆'
    TWO = 2, '★★☆☆☆'
    THREE = 3, '★★★☆☆'
    FOUR = 4, '★★★★☆'
    FIVE = 5, '★★★★★'

class Item(TimeStampedModel):
    item_id = UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    item_name = models.CharField(max_length=64)
    item_feature = models.TextField(max_length=512)

class Review(TimeStampedModel):
    review_id = UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    review_from = ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    review_about = ForeignKey(Item, on_delete=models.CASCADE, db_column="item_id")
    review_text = models.TextField(max_length=512)
    review_rating = models.IntegerField(choices=Rating_star, validators=[MinValueValidator(1), MaxValueValidator(5)],default=Rating_star.THREE)

