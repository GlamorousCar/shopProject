from shop.models import Product
from shop.models import Category
from shop.models import Gallery
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from mail_sending.forms import ContactModelForm
from django.http import JsonResponse


def index(request):
    form = ContactModelForm()
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })

    products = Product.objects.order_by('-created_at')[:12]

    return render(request, 'index.html', {'products': products, 'form': form})


def category_view(request, slug):
    form = ContactModelForm()
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    category = get_object_or_404(Category, slug=slug)
    products_list = category.get_products.order_by('id')
    paginator = Paginator(products_list, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'products': products, 'form': form})


def item_view(request, name, slug):
    products = Product.objects.get(slug=slug)

    cart_product_form = CartAddProductForm()

    return render(request, 'item-page.html', {'products': products, 'cart_product_form': cart_product_form})


def sale_view(request):
    products = Product.objects.filter(sale=True)
    return render(request, 'index.html', {'products': products})


def exclusive_view(request):
    products = Product.objects.filter(exclusive=True)
    return render(request, 'index.html', {'products': products})


def cart(request):
    return render(request, 'cart.html')
