from __future__ import absolute_import
from django.contrib import admin
from .models import Configuration, Locale, MarketingSites


class MarketingSitesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MarketingSites._meta.get_fields()]
    readonly_fields = (
        u"created",
        u"updated",
    )


class LocaleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Locale._meta.get_fields()]
    readonly_fields = (
        u"created",
        u"updated",
    )


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Configuration._meta.get_fields()]

    readonly_fields = (
        u"created",
        u"updated",
    )


admin.site.register(MarketingSites, MarketingSitesAdmin)
admin.site.register(Locale, LocaleAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
