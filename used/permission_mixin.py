from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from accounts.models import CustomUser


class MyTestUserPassesTest(UserPassesTestMixin): #czy nalezy do jakiejs grupy

    def test_func(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect('login')
