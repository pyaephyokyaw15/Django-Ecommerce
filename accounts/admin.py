from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .forms import AccountCreationForm
from django.utils.html import format_html

class AccountAdmin(UserAdmin):
    # exclude = ('username', )
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    add_form = AccountCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
         ),
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {
            'classes': ('wide',),
            'fields': ('profile_picture', )}
         ),
    )




admin.site.register(Account, AccountAdmin)
