from shop.models import Category
#from mail_sending.forms import ContactModelForm
from django.http import JsonResponse

def category(request):
    return {"categories": Category.objects.all()}
