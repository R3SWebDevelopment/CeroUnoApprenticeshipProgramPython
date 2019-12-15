from django.contrib import admin
from django.contrib.auth import get_user_model

from doorstep.admin import ModelAdmin


class UserAdmin(ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'is_verified',)
    list_filter = ('gender', 'created_on',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    date_hierarchy = 'created_on'


admin.site.register(get_user_model(), UserAdmin)
