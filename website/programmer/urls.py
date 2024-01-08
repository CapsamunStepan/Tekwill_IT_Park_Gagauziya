from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'programmer'

urlpatterns = [
    path('home/', views.home_view, name='programmer_home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home:home'), name='logout'),
    path('create_portfolio/', views.create_portfolio, name='create_portfolio'),
    path('view_portfolio/', views.view_portfolio, name='view_portfolio'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('news/', views.news_view, name='news_view'),
    path('taken_orders/', views.taken_orders, name='taken_orders'),
    path('contacts/', views.contacts, name='contacts'),
    path('portfolio/', views.edit_portfolio, name='edit_portfolio'),
    path('profile/', views.view_profile, name='view_profile'),
    path('take_order/', views.take_order, name='take_order'),
    path('delete_order/', views.delete_order, name='delete_order'),
    path('order/<int:order_id>/', views.view_order_detail, name='order_detail'),
]
