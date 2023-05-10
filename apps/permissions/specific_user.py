from rest_framework.permissions import BasePermission
from rest_framework import permissions


class AdminUserPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous and request.user.email == 'admin@gmail.com')


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
