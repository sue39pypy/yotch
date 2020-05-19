from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe

import os

def get_image_path(instance, filename):
    """画像パスの設定
    :param instance: Wallpaperインスタンス
    :param filename: 元ファイル名
    :return: 設定したファイル名含む該当画像ファイルパス
    """
    name = filename
    path = instance.__class__.__name__.lower() + 's/'
    return path + name

class Wallpaper(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='壁紙名称'
    )
    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name='壁紙画像'
    )
    caption = models.TextField(
        verbose_name='壁紙説明'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日時'
    )

    def get_image_source(self):
        """画像ファイルアップロードパスを取得
        :param self: Wallpaperインスタンス
        :return    : 画像ファイルアップロードパス
        """
        return os.path.join('/', settings.MEDIA_URL, str(self.image))

    def admin_wallpaper_image(self):
        """adminのリスト表示ページのサムネイルをスタイル調整して表示
        :param self: Wallpaperインスタンス
        :return    : mark_safeメソッド実行結果
        """
        if self.image:
            return mark_safe('<img src="{}" style="width:50px;height:50px;">'.format(self.get_image_source()))
        else:
            return 'no image'

    admin_wallpaper_image.short_description = 'Image'
    admin_wallpaper_image.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
