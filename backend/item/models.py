from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import logging
from django.db import models
import os
import sys
import uuid

from utils.models import ImageModel

def check_flg_item(value):
    if value != 0 and value != 1:
        raise ValidationError('入力が不適切です。')

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

class Dish(ImageModel):
    """
    Aboutページ内Cookingコンテンツ内表示項目

    properties
    title : str
        料理名
    image : str
        イメージ参照パス
    caption : str
        説明
    url : str
        URL
    rank : int
        並び順
    created_at : datetime
        作成日時
    updated_at : datetime
        更新日時
    """
    title = models.CharField(
        max_length=50,
        verbose_name='料理名'
    )
    caption = models.TextField(
        verbose_name='説明'
    )
    url = models.TextField(
        blank=True,
        null=True,
        verbose_name='URL'
    )
    rank = models.IntegerField(
        verbose_name='並び順',
        validators=[MinValueValidator(0)]
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

class Interior(ImageModel):
    """
    Aboutページ内Interiorコンテンツ表示項目
    properties
    title : str
        イメージタイトル
    image : str
        イメージ参照パス
    rank : int
        ランク（表示順序等に利用）
    description : str
        キャプション（現時点では用途なし）
    created_at : datetime
        作成日時
    updated_at : datetime
        更新日時
    """
    title = models.CharField(
        max_length=20,
        verbose_name='タイトル'
    )
    rank = models.IntegerField(
        verbose_name='ランク',
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0)]
    )
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

class Skill(models.Model):
    """
    Skill項目クラス

    properties
    name : str
        技術名称
    icon : str
        font-awesomeの識別クラス
    level : int
        技術レベル（0〜3）
    caption : str
        説明
    rank : int
        並び順
    created_at : datetime
        作成日時
    updated_at : datetime
        更新日時
    """

    name = models.CharField(
        max_length=50,
        verbose_name='名称'
    )
    icon = models.CharField(
        max_length=50,
        verbose_name='アイコンクラス'
    )
    level = models.IntegerField(
        verbose_name='レベル',
        validators=[MinValueValidator(0), MaxValueValidator(3)]
    )
    caption = models.TextField(
        verbose_name='説明'
    )
    rank = models.IntegerField(
        verbose_name='並び順',
        validators=[MinValueValidator(0)]
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
        ordering = ('rank',)

class Slide(ImageModel):
    """
    Aboutページ内コンテンツスライドクラス

    properties
    title : str
        スライドタイトル
    image : str
        イメージ参照パス
    rank : int
        ランク（表示順序等に利用）
    description : str
        キャプション
    created_at : datetime
        作成日時
    updated_at : datetime
        更新日時
    """
    title = models.CharField(
        max_length=20,
        verbose_name='タイトル'
    )
    rank = models.IntegerField(
        verbose_name='ランク',
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField(
        verbose_name='概要',
        blank=True,
        null=True
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
    """
    ページ内に表示する壁紙クラス

    properties
    name : str
        スライドタイトル
    image : str
        イメージ参照パス
    caption : str
        キャプション
    created_at : datetime
        作成日時
    updated_at : datetime
        更新日時
    """
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
