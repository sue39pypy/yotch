from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

def check_flg_item(value):
    if value != 0 and value != 1:
        raise ValidationError('入力が不適切です。')

class Information(models.Model):
    """
    基本情報管理クラス

    name : str
        SNS名称
    name_ja : str
        和名
    type : str
        情報種別
        'account' : SNSアカウント
        'info'    : 連絡先等の基本情報
    value : str
        氏名、連絡先、アカウントID等の情報
    url : str
        アカウントトップページURL
    icon : str
        font-awesomeアイコンの識別class
    color : str
        画面描画時の背景色
    rank : int
        並び順
    created_at : datetime
        作成日時
    updated_at : datetime
        更新日時
    """
    name = models.CharField(
        max_length=50,
        verbose_name='サービス名称'
    )
    name_ja = models.CharField(
        max_length=50,
        verbose_name='和名',
        blank=True,
        null=True
    )
    type = models.CharField(
        max_length=50,
        verbose_name='情報種別'
    )
    value = models.CharField(
        max_length=255,
        verbose_name='値'
    )
    url = models.TextField(
        verbose_name='URL',
        blank=True,
        null=True
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='アイコンクラス'
    )
    color = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='背景色'
    )
    rank = models.IntegerField(
        verbose_name='ランク',
        blank=False,
        null=False,
        default=0,
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