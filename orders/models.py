from django.db import models

# Create your models here.
from django.db import models
from shop.models import Product
from  django.db.models.signals import post_save
from django.core.mail import send_mail
from django.http import HttpResponse

class Order(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50,verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    address = models.CharField(max_length=250,verbose_name='Адрес')
    postal_code = models.CharField(max_length=20,verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100,verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    def order_email(self):
        return self.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


def post_save_dis(sender,**kwargs):
    client_data = kwargs['instance'].order
    order_product= kwargs['instance'].product
    email = send_mail("Новый заказ", f"Заказ от {client_data.first_name} {client_data.last_name} \n Почтовый адрес: {client_data.email} \n По адресу: {client_data.city} {client_data.address} \n Заказ: {order_product}",  "prynikvany@gmail.com", ['Dr.JohnYu@yandex.ru'])
    #print('All is ok')
post_save.connect(post_save_dis,sender=OrderItem)