from django.contrib import admin
from .models import Order
from .models import Comment


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'title', 'full_subscription')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'text', 'created')
