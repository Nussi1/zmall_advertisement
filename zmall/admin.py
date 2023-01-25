from django.contrib import admin
from user.models import User, ActivationCode


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(ActivationCode)
