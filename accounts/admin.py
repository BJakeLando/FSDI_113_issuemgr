from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role, Team, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display=[
        "username", "email", "first_name", "last_name",
        'role', 'team', 'is_staff'
    ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "team")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register([Role,Team])