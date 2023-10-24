# Python

# Django
from django.core.mail import send_mail
from django.conf import settings

# Project
from apps.user.models import User
from apps.main.news.models import News
from apps.messages import msg


def make_email_verify_msg(lang='EN'):
    return {
        "subject": msg.SUBJECT[lang],
        "otp_code": msg.OTP_CODE,
        "message": msg.MESSAGE[lang]
    }


def send_otp_via_email(email, lang='EN'):
    try:
        message = make_email_verify_msg(lang=lang.upper())
        email_from = settings.EMAIL_FROM
        user_obj = User.objects.get(email=email)
        send_mail(f"{message['subject']}", f"{message['message']}", email_from, [user_obj.email], fail_silently=False)
        user_obj.otp = message['otp_code']
        user_obj.save()
        return user_obj
    except Exception as ex:
        return {'status': 400, 'error': ex}


def send_mailing_email(subject, message, email_from):
    for item in User.objects.filter(send_news=True):
        send_mail(f'"{subject}"', f'"{message}"', email_from, [item.email], fail_silently=True)
