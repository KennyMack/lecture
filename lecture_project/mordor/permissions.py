__author__ = 'jonathan'
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request)

        if request.method in permissions.SAFE_METHODS:
            return True

        return  obj.owner == request.user