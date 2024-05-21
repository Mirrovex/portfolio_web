from django.contrib import admin

from .models import Settings, Page


class PageAdmin(admin.ModelAdmin):

    list_display = ('name', 'order', 'reverse_url', 'slug')
    search_fields = ("name", )
    list_editable = ('order',)



admin.site.register(Settings)
admin.site.register(Page, PageAdmin)