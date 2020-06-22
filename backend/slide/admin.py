from django.contrib import admin
from .models import Slide

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'rank', 'admin_slide_image')

    def _meta(self, row):
        return ','.join([x.title for x in row.meta.all()])

admin.site.register(Slide, SlideAdmin)