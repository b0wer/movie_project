from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email', 'text')
        model = Reviews
