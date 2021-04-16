from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from users.models import User, Association

admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(Association)
admin.site.unregister(Group)
