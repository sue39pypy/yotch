from django.contrib import admin

from .models import Information

# Register your models here.

class InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'value', 'url', 'icon', 'rank')
    ordering = ('rank',)

    def _meta(self, row):
        return ','.join([x.name for x in row.meta.all()])

admin.site.register(Information, InformationAdmin)