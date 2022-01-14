from __future__ import absolute_import
from django.contrib import admin
from .models import Configuration, Locale

class LocaleAdmin(admin.ModelAdmin):
    list_display = (
        "element_id",
        "lang",
        "url",
        "value",
    )
    readonly_fields = (
        u"created",
        u"updated",
    )

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "stepwise_host",
        "created",
        "updated",
    )
    readonly_fields = (
        u"created",
        u"updated",
    )

admin.site.register(Locale, LocaleAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
