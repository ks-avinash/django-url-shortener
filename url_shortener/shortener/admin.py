from django.contrib import admin

from .models import ShortURL


# Register your models here.


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'url', 'created_date', 'count')
    ordering = ('-created_date',)


admin.site.register(ShortURL, UrlsAdmin)
