from django.contrib import admin
from .models import Wallpaper

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'admin_wallpaper_image')

    def _meta(self, row):
        return ','.join([x.name for x in row.meta.all()])

admin.site.register(Wallpaper, WallpaperAdmin)