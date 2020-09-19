from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
import logging
import os
import sys
import uuid

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

class ImageModel(models.Model):
    # スライド画像
    image = models.ImageField(
        upload_to=get_image_path,
        blank=True,
        null=True,
        verbose_name='画像'
    )

    class Meta:
        abstract = True

    def get_image_source(self):
        """画像ファイルアップロードパスを取得
        :param self: インスタンス
        :return    : 画像ファイルアップロードパス
        """
        return os.path.join('/', settings.MEDIA_URL, str(self.image))

    def admin_image(self):
        """adminのリスト表示ページのサムネイルをスタイル調整して表示
        :param self: インスタンス
        :return    : mark_safeメソッド実行結果
        """
        if self.image:
            return mark_safe('<img src="{}" style="width:50px;height:50px;">'.format(self.get_image_source()))
        else:
            return 'no image'

    admin_image.short_description = 'Image'
    admin_image.allow_tags = True