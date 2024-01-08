from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('news', views.news_view, name='news_view')
]

