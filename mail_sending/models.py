from django.db import models
from django import forms
#<div class="col-7 col-sm-7 col-md-8 col-lg-8 col-xl-8" style="max-width: auto;width: 100%;margin-left: 0px;"><input type="text" class= style="background-color: rgb(237,237,237);padding-top: 0px;padding-bottom: 0px;width: 100%;height: 100%;" placeholder="E-mail"></div>

# Create your models here.
from django.db import models



# Create your models here.


class Contact(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'почтовые адреса'
        verbose_name = 'почтовый адрес'