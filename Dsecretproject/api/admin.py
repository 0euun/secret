from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class CustomUserAdmin(BaseUserAdmin):
    # 기존 필드 + nickname을 추가
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('nickname',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {'fields': ('nickname',)}),
    )
    list_display = BaseUserAdmin.list_display + ('nickname',)

admin.site.register(User, CustomUserAdmin)