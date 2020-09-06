from django.contrib import admin
from .models import Dish, Skill, Slide, Wallpaper

class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'caption', 'url', 'rank', 'admin_image')
    ordering = ('rank', )

    def _meta(self, row):
        return ','.join([x.title for x in row.meta.all()])

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'level', 'caption', 'rank')
    ordering = ('rank', )

    def _meta(self, row):
        return ','.join([x.name for x in row.meta.all()])

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'rank', 'admin_image')
    ordering = ('rank', )

    def _meta(self, row):
        return ','.join([x.title for x in row.meta.all()])

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'admin_image')

    def _meta(self, row):
        return ','.join([x.name for x in row.meta.all()])

admin.site.register(Dish, DishAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Wallpaper, WallpaperAdmin)