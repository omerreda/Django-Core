from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import NewUser, Profile


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username',
                           'first_name', 'last_name', 'password')}),
        ('Email', {'fields': ('email',)}),
        ('Custom Bar', {'fields': ('city',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(NewUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(Profile)
