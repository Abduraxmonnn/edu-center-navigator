# Django
from django.db import models

# Project
from apps.main.center.models import Center
from apps.user.models import User


class CommentHelper(models.Model):
    """
    This used to save information of a comment owner and text...
    :owner: This field connected to User as foreign for determine an owner of comment
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    is_updated = models.BooleanField(
        default=False
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.owner.name

    class Meta:
        verbose_name = 'Comment Helper'
        verbose_name_plural = 'Comment Helpers'


class Comment(models.Model):
    """
    This main model used to save Comments.
    :comment_helper: This field connected to CommentHelper as ForeignKey
    :comment_helper: This field connected to Center as ForeignKey
    for get data of owner, text... and center for get information about Center.
    """
    comment_helper = models.ForeignKey(
        CommentHelper,
        on_delete=models.CASCADE
    )
    center = models.ForeignKey(
        Center,
        on_delete=models.CASCADE
    )
    is_updated = models.BooleanField(
        default=False
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.comment_helper.owner} {self.comment_helper.text} {self.center}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
