from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (*UserAdmin.fieldsets, ('Exteded Personal info', {
        'fields': (
            'phone_number',
            'id_number',
            'address',
            'id_copy',
            'proof_of_address',
        )
    }))


admin.site.register(CustomUser, CustomUserAdmin)
