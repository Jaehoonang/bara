from django import forms
from .models import Review, Item

class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ItemPostForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
