# Project
from config.celery import app
from apps.main.news.models import News
from apps.emails.send_email_via.send_email import send_mailing_email


@app.task()
def send_mailing_email_task():
    news = News.objects.all().last()
    send_mailing_email(news.subject, news.message, news.email_from)


@app.task(bind=True, default_retry_delay=60)
def retry_task(self, x, y):
    count = 0
    try:
        return x + y
    except Exception as exc:
        count += 1
        if count >= 3:
            return exc
        raise self.retry(exc=exc, countdown=60)
