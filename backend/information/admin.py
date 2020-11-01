from django.contrib import admin

from .models import Information

# Register your models here.

class InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_ja', 'type', 'value', 'url', 'icon', 'color', 'rank')
    ordering = ('rank',)

    def _meta(self, row):
        return ','.join([x.name for x in row.meta.all()])

admin.site.register(Information, InformationAdmin)