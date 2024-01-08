from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import OrderForm, CommentForm
from .models import Order
from programmer.models import Portfolio
from home.models import News


# Create your views here.
@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def home_view(request):
    return render(request, 'customer/home.html')


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def create_order(request):
    try:
        order = Order.objects.filter(user_id=request.user.id).order_by('-created')[0]
        order_id = order.order_id
    except:
        order_id = 0
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.user_id = request.user.id
            form.instance.order_id = order_id + 1
            form.save()
            orders = Order.objects.filter(user_id=request.user.id).order_by('-created')
            return render(request, 'customer/order_view.html', {'orders': orders})
    else:
        form = OrderForm()

    return render(request, 'customer/create_order.html', {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def edit_order(request):
    pass


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def delete_order(request):
    pass


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def view_orders(request):
    orders = Order.objects.filter(user_id=request.user.id).order_by('-created')
    return render(request, 'customer/order_view.html', {'orders': orders})


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def view_programmers(request):
    programmers = Portfolio.objects.all()
    return render(request, 'customer/view_programmers.html', {'programmers': programmers})


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def news_view(request):
    news = News.objects.filter().order_by('-published')
    return render(request, 'customer/news_view.html', {'news': news})


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def page_is_not_found(request):
    return render(request, 'customer/404.html')


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def handler404_(request, exception):
    return render(request, 'customer/404.html', status=404)


@user_passes_test(lambda u: u.groups.filter(name='Заказчик').exists())
def view_order_detail(request, order_id):
    # order_id = request.POST.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if order.user != request.user:
        return render(request,
                      'customer/view_order_detail.html',
                      {"access_denied": True})

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.order = order
            form.instance.user = request.user
            form.save()
            form = CommentForm()
    else:
        form = CommentForm()
    comments = order.comments.all()
    return render(request, 'customer/view_order_detail.html',
                  {"order": order,
                   "comments": comments,
                   "form": form})
