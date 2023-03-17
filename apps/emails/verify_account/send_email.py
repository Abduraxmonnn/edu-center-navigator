# Python
import json
import random

# Django
from django.core.mail import send_mail
from django.conf import settings

# Project
from apps.user.models import User
from messages import msg


def make_email_verify_msg():
    otp = random.randint(100000, 999999)
    msg.OTP_CODE = otp
    return {
        "subject": msg.SUBJECT,
        "otp_code": otp,
        "message": msg.MESSAGE
    }

def send_otp_via_email(email):
    msg = make_email_verify_msg()
    email_from = settings.EMAIL_FROM
    user_obj = User.objects.get(email=email)
    send_mail(msg['subject'], msg['message'], email_from, [user_obj.email], fail_silently=False)
    user_obj.otp = msg['otp_code']
    user_obj.save()
    return user_obj
