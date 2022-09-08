from django.contrib import admin

from shortenersite.models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'pub_date', 'count')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)
