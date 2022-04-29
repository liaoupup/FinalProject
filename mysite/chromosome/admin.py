from django.contrib import admin
from .models import AbnormalType, Abnormal


@admin.register(AbnormalType)
class AbnormalTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Abnormal)
class AbnormalAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'description', 'karyotype', 'broken_site', 'get_read_num', 'fragile_site', 'chromosome', 'author')
