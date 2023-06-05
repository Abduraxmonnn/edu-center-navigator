# Project
from config.celery import app
from apps.main.news.models import News
from apps.emails.send_email_via.send_email import send_mailing_email


@app.task()
def send_mailing_email_task():
    news = News.objects.all().last()
    send_mailing_email(news.subject, news.message, news.email_from)
