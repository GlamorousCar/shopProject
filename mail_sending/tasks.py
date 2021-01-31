from shopProject.celery import app
from django.core.mail import EmailMessage, get_connection


@app.task()
def send_mail_task(text, queryset):
    queryset = [value for d in queryset for key, value in d.items() if key == 'email']
    con = get_connection()
    con.open()
    mail = EmailMessage('subject', text, 'prynikvany@gmail.com',bcc=queryset)
    mail.send()
    con.close()
    return {"status": True}

# 127.0.0.1:6379
