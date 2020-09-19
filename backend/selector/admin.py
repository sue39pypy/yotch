from django.contrib import admin
from .models import Selector

class SelectorAdmin(admin.ModelAdmin):
    list_display = ( 'label', 'value', 'type', 'rank')

    def _meta(self, row):
        return ','.join([x.label for x in row.meta.all()])

admin.site.register(Selector, SelectorAdmin)