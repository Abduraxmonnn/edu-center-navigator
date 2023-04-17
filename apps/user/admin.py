# Django
from django.contrib import admin

# Project
from apps.user.models import User


admin.site.register(User)
