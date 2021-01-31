

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SendMailForm
# Register your models here.
from .models import Contact
from .tasks import send_mail_task


# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    actions = ('send_emails',)

    def send_emails(self, request, queryset):
        form = None
        if 'apply' in request.POST:
            form = SendMailForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['message']
                data = list(queryset.values())
                task = send_mail_task.delay(text=text, queryset=data)
                # TODO отправку красивых писем читать EmailMultiAlternatives
                self.message_user(request, "Письма успешно доставлены адресатам")

                return HttpResponseRedirect(request.get_full_path())

        if not form:
            form = SendMailForm(initial={'_selected_action': queryset.values_list('id', flat=True)})

        return render(request, 'sendemail.html',
                      {'items': queryset, 'form': form, 'title': u'Изменение категории'})

    send_emails.short_description = "Разослать письмо адресатам"


admin.site.register(Contact, EmailAdmin)

# 4.189391136169434
# 2.2064855098724365
