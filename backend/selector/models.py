from django.conf import settings
from django.core.validators import MinValueValidator
import logging
from django.db import models
import os
import sys
import uuid

#選択肢マスタモデル
class Selector(models.Model):
    # タイプ
    type = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='タイプ'
    )
    # 選択値
    value = models.IntegerField(
        verbose_name='選択値',
        blank=False,
        null=False,
        validators=[MinValueValidator(0)]
    )
    # ラベル
    label = models.CharField(
        max_length=20,
        verbose_name='ラベル'
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
    # 有効・無効
    status = models.IntegerField(
        verbose_name='有効・無効',
        blank=False,
        null=False,
        default=1
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
        return "{}({})".format(self.label, self.value)

    class Meta:
        ordering = ('rank',)