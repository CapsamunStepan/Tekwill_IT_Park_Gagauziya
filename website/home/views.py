from django.shortcuts import render, redirect
from .models import News


def news_view(request):
    news = News.objects.filter().order_by('-published')
    if request.user.groups.filter(name='Программист').exists():
        return redirect(to='programmer:news_view')
    elif request.user.groups.filter(name='Заказчик').exists():
        return redirect(to='customer:news_view')
    else:
        return render(request, 'home/news_view.html', {'news': news})


# Create your views here.
def home_view(request):
    if request.user.groups.filter(name='Программист').exists():
        return redirect(to='programmer:programmer_home')
    elif request.user.groups.filter(name='Заказчик').exists():
        return redirect(to='customer:customer_home')
    else:
        return render(request, 'home/home.html')
