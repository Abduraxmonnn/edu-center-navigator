# Django
from django.db import models

# Project
from apps.courses.models import CourseCategory, Course
from apps.address.models import Address
from apps.teacher.models import Teacher
from apps.user.models import User


class Center(models.Model):
    """
    This main model of Project is used to save information about Centers.
    :references: 4
    :center_address: This field connected to Address as ForeignKey for determine Address of Center
    :main_course: This field connected to CourseCategory as ForeignKey for determine Category of Course
    :top_teachers: This field connected to Teacher as ManyToMany for determine all Teachers of Center
    :courses: This field connected to Category as ManyToMany for determine all Courses of Center
    """
    name = models.CharField(
        max_length=255,
        unique=True
    )
    center_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True
    )
    main_course = models.ForeignKey(
        CourseCategory,
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    top_teacher = models.ManyToManyField(
        Teacher
    )
    courses = models.ManyToManyField(
        Course
    )
    is_public = models.BooleanField(
        default=False
    )
    visited = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )
    score = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )
    created_date = models.DateField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.image} {self.name} {self.main_course} {self.is_public} {self.score}'

    class Meta:
        verbose_name = 'Center'
        verbose_name_plural = 'Centers'


class CenterUserRelationship(models.Model):
    center_id = models.ForeignKey(
        Center,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    in_save = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.center_id.name} {self.user_id.username} {self.in_save}'

    class Meta:
        verbose_name = 'Centers liked by users'
