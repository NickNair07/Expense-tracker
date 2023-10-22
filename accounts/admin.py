from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm


# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_active', 'is_staff')}),
        ('Personal info', {'fields': ('username',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)