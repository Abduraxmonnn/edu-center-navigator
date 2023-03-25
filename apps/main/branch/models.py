# Django
from django.db import models

# Project
from apps.main.address.models import Address
from apps.main.courses.models import Course
from apps.main.center.models import Center
from apps.user.models import User


class Branch(models.Model):
    """
    This model is used to save information about Center Branches.
    :references: 3
    :branch_address: This field connected to Address as ForeignKey for determine Address of Center
    :center: This field connected to Center as ForeignKey
    :top_teachers: This field connected to Teacher as ManyToMany for determine all Teachers of Center
    :courses: This field connected to Category as ManyToMany for determine all Courses of Center
    """
    name = models.CharField(
        max_length=255
    )
    slug = models.CharField(
        max_length=155,
        blank=True,
        null=True
    )
    center = models.ForeignKey(
        Center,
        on_delete=models.CASCADE
    )
    branch_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.ImageField(
        upload_to='branches/%Y/%m'
    )
    courses = models.ManyToManyField(
        Course
    )
    visited = models.IntegerField(
        blank=True,
        null=True
    )
    score = models.IntegerField(
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        default=False
    )
    created_date = models.DateField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.image} {self.name} {self.is_public} {self.score}'

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'


class BranchUserRelationship(models.Model):
    branch_id = models.ForeignKey(
        Branch,
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
        return f'{self.branch_id.name} {self.user_id.username} {self.in_save}'

    class Meta:
        verbose_name = 'Branches liked by users'
