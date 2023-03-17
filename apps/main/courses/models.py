# Django
from django.db import models


class CourseCategory(models.Model):
    """
    This model for Category of Course and this used to for identify of main course of each Center (Branch).
    """
    name = models.CharField(
        max_length=255
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Courses Categories'


class Course(models.Model):
    """
    This is main Course model,
    This used to save each course of each Centers (Branch).
    :category: This field connected to CourseCategory as ForeignKey for determine Category of Course
    """
    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255
    )
    price = models.FloatField()
    course_duration = models.IntegerField()
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.category} {self.name} {self.price} {self.course_duration}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
