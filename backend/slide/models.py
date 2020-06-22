from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe
import logging
import sys

from django.db import models

import os
import sys
import uuid

def get_image_path(instance, filename):
    """画像パスの設定
    :param instance: Slideインスタンス
    :param filename: 元ファイル名
    :return: 設定したファイル名含む該当画像ファイルパス
    """
    try:
        logger = logging.getLogger('')

        name = str(uuid.uuid4()).replace('-', '')
        path = instance.__class__.__name__.lower() + 's/'
        extension = os.path.splitext(filename)[-1]
        return path + name + extension
    except:
        function_name = sys._getframe().f_code.co_name
        log_message = function_name + '\n'\
                      + sys.exc_info()
        logger.error(log_message)

class Slide(models.Model):
    # スライドタイトル
    title = models.CharField(
        max_length=20,
        verbose_name='タイトル'
    )
    # スライド画像
    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name='画像'
    )
    # ランク（表示順序等に利用）
    rank = models.IntegerField(
        verbose_name='ランク',
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0)]
    )
    # キャプション（現時点では用途なし）
    caption = models.TextField(
        verbose_name='概要',
        blank=True,
        null=True,
        max_length=1000
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
        :param self: Slideインスタンス
        :return    : 画像ファイルアップロードパス
        """
        return os.path.join('/', settings.MEDIA_URL, str(self.image))

    def admin_slide_image(self):
        """adminのリスト表示ページのサムネイルをスタイル調整して表示
        :param self: Slideインスタンス
        :return    : mark_safeメソッド実行結果
        """
        if self.image:
            return mark_safe('<img src="{}" style="width:50px;height:50px;">'.format(self.get_image_source()))
        else:
            return 'no image'

    admin_slide_image.short_description = 'Image'
    admin_slide_image.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('rank',)