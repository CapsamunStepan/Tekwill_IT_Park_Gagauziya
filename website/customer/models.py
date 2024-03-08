from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    order_id = models.IntegerField(default=1)
    title = models.CharField(max_length=250)
    full_subscription = models.TextField()
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    programmer = models.ForeignKey(User,
                                   on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='programmer_orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    taken = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.order.title}"