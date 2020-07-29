from django.conf import settings

from rest_framework.permissions import BasePermission


class CheckAPIKEY(BasePermission):
    def has_permission(self, request, view):
        api_key_secret = request.headers['Secret']
        return api_key_secret == settings.API_SECRET
