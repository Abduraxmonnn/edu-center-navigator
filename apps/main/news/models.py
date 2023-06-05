# Python
import os

# Django
from django.db import models


class News(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    file = models.FileField(blank=True, null=True)
    email_from = models.CharField(max_length=100, default=os.getenv('EMAIL_FROM'))
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
