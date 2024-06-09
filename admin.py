from django.contrib import admin
from .models import *


@admin.register(CustomUser)
class CustomUserUserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'first_name', 'last_name',)
    # list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_display = ('phone_number', 'email', 'otp','is_superuser', 'is_active')


from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(ServiceType)
admin.site.register(Facility)
admin.site.register(Vendor)
admin.site.register(MainCategory)