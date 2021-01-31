from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from mail_sending.models import Contact
from shop.models import Product

from shop.views import Category

from django.core.mail import send_mail
from django.http import HttpResponse

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                item['product'].Instock = False
                item['product'].save()
                #get_name = Product.objects.filter(id=item['product']['id']).update(Instock=False)
            cart.clear()
            # очистка корзины
            new_contact = Contact.objects.create(email=str(order.order_email()))
            return render(request, 'order-created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order.html',
                  {'cart': cart, 'form': form})