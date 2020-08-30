from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('id', 'first_name', 'email', 'company', 'title')
    list_display = ('id', 'first_name', 'email', 'company', 'title')
    list_filter = ('company',)
    ordering = ('first_name',)
