from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    # exclude = ('username', )
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
         ),
    )
    # list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    # list_display_links = ('email', 'first_name', 'last_name')
    # readonly_fields = ('last_login', 'date_joined')
    # ordering = ('-date_joined',)
    #
    # filter_horizontal = ()
    # list_filter = ()
    # fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))

    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)