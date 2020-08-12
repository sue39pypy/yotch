from django.contrib import admin
from .models import Interior
from .models import Slide
from .models import Wallpaper

class InteriorAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'rank', 'admin_image')

    def _meta(self, row):
        return ','.join([x.title for x in row.meta.all()])

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'rank', 'admin_image')

    def _meta(self, row):
        return ','.join([x.title for x in row.meta.all()])

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'admin_image')

    def _meta(self, row):
        return ','.join([x.name for x in row.meta.all()])

admin.site.register(Interior, InteriorAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Wallpaper, WallpaperAdmin)