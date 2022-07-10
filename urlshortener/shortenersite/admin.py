from django.contrib import admin
from shortenersite.models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'pub_date', 'count')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)
