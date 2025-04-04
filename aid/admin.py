from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'submitted_at')
    search_fields = ('full_name', 'phone_number', 'message')
