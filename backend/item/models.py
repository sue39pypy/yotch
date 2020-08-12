from django.conf import settings
from django.core.validators import MinValueValidator
import logging
from django.db import models
import os
import sys
import uuid

from utils.models import ImageModel

def get_image_path(instance, filename):
    """画像パスの設定
    :param instance: インスタンス
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

class Interior(ImageModel):
    # スライドタイトル
    title = models.CharField(
        max_length=20,
        verbose_name='タイトル'
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
    description = models.TextField(
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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('rank',)

class Slide(ImageModel):
    # スライドタイトル
    title = models.CharField(
        max_length=20,
        verbose_name='タイトル'
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
    description = models.TextField(
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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('rank',)

class Wallpaper(ImageModel):
    name = models.CharField(
        max_length=50,
        verbose_name='壁紙名称'
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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
