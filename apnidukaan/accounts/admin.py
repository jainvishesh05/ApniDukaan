from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Address , CustomUser

# Register your models here.
admin.site.register(CustomUser)
class CustomUserUser(UserAdmin):
    list_display = ['username' , 'phone_number']
    search_fields = ['username' , 'phone_number']
    fieldsets = UserAdmin.fieldsets + (('Extra Info', {'fields': ('phone_number',)}),)  # type: ignore
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {"fields": ("phone_number",)}),
    )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user' , 'city' , 'postal_code' , 'is_default']
    search_fields = ['user__username' , 'city']