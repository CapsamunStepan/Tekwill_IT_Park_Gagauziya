from django import forms
from .models import Order
from .models import Comment


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', "full_subscription", 'price']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
