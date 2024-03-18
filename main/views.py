from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

def index_view(request):
    banner = Products.objects.filter(is_banner=True).order_by('-id')[:3]
    shop_collections = Products.objects.filter(shop_collections=True).order_by('-id')[:6]
    featured_product = Products.objects.filter(featured_product=True).order_by('-id')[:8]
    new_product = Products.objects.filter(new_product=True).order_by('-id')[:8]
    is_advert = Products.objects.filter(is_advert=True).order_by('-id')[:2]
    if request.user.is_authenticated:
        basket_count = Basket.objects.filter(user=request.user).count()
    else:
        basket_count = 0
    contex = {
        'banner': banner,
        'shop_collection': shop_collections,
        'products': featured_product,
        'new_products': new_product,
        'is_advert': is_advert,
        'brand': Brand.objects.all().order_by('-id')[:7],
        'contact': Contact.objects.last(),
        'basket_count': basket_count
    }
    return render(request, "index.html", contex)

def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    related = Products.objects.filter(category=product.category).order_by('-id')[:4]
    basket_count = Basket.objects.filter(user=request.user).count()
    context ={
        'product': product,
        'related': related,
        'contact': Contact.objects.last(),
        'basket_count': basket_count
    }
    return render(request, 'productDetails.html', context)


def product(request):
    product = Products.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    basket_count = Basket.objects.filter(user=request.user).count()
    context = {
        'product':product,
        'category':category,
        'brand':brand,
        'basket_count':basket_count
    }
    return render(request, "products.html", context)

@login_required(login_url='/login/')
def add_basket(request, pk):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login_url')
    product = Products.objects.get(pk=pk)
    Basket.objects.create(
        user=user,
        product=product,
    )
    return HttpResponse("Item added to basket successfully!")



@login_required(login_url='/login/')
def add_basket_form(request, pk):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login_url')
    number = request.POST.get('number')
    product = Products.objects.get(pk=pk)
    for _ in number:
        Basket.objects.create(
            user=user,
            product=product,
        )
    return redirect('product_detail_url', pk=pk)

@login_required(login_url='/login/')
def remove_cart_product(request, pk):
    basket = Basket.objects.get(pk=pk)
    basket.delete()
    return redirect('cart_url', pk=request.user.id)



@login_required(login_url='/login/')
def cart(request, pk):
    basket = Basket.objects.filter(user_id=pk)
    basket_count = Basket.objects.filter(user_id=pk).count()
    subtotal = 0
    for i in basket:
        subtotal += i.product.price
    tax = subtotal * (1 / 100)
    total = subtotal+tax
    context = {
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='/login/')
def create_total_sum(request,):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login_url')
    basket = Basket.objects.filter(user_id=user.id)
    product_counts = basket.values('product').annotate(count=Count('id'))
    duplicate_products = [(product_count['product'], product_count['count']) for product_count in product_counts]
    products = ''
    for product_id, count in duplicate_products:
        product_name = Products.objects.get(id=product_id)
        products += f"Mahsulot nomi: {product_name.title}, Mahsulotlar soni: {count}\n"
    subtotal = 0
    for i in basket:
        subtotal += i.product.price
    tax = subtotal * (1 / 100)
    total = subtotal+tax
    TotalSum.objects.create(
        user=user,
        products=products,
        sub_total=subtotal,
        tax=tax,
        total_expenses=total
        )
    return redirect('index_url')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(
            username=username,
            password=password
        )
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
        else:
            context = {
                'error': True
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')

def sing_up_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            context = {
                'band': True,
            }
            return render(request, 'sing-up.html', context)
        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('index_url')

    return render(request, 'sing-up.html')

def user_logout(request):
    logout(request)
    return redirect('index_url')
