from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'customer'

urlpatterns = [
    path('home/', views.home_view, name='customer_home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home:home'), name='logout'),
    path('create_order/', views.create_order, name="create_order"),
    path('edit_order/', views.edit_order, name='edit_order'),
    path('delete_order/', views.delete_order, name='delete_order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('view_programmers/', views.view_programmers, name='view_programmers'),
    path('news/', views.news_view, name='news_view'),
    path('404/', views.page_is_not_found, name='404'),
    path('order/<int:order_id>/', views.view_order_detail, name='order_detail'),

]


