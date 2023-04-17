# Django
from django.db import models


class Teacher(models.Model):
    """
    This model is used to save Top Teachers of Each Centers.1
    """
    name = models.CharField(
        max_length=255
    )
    description = models.TextField()
    experience_year = models.FloatField()
    image = models.ImageField(
        upload_to='Teachers/%Y/%m',
        blank=True,
        null=True,
    )
    number_students = models.IntegerField()

    def __str__(self):
        return f'{self.image} {self.name} {self.experience_year}'

    class Meta:
        verbose_name = 'Top Teacher'
        verbose_name_plural = 'Top Teachers'
