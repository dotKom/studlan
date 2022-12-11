# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from apps.lan.models import LAN


class Article(models.Model):
    pub_date = models.DateTimeField(_(u'date published'), default=datetime.now, blank=True, null=True)
    relevant_to = models.ManyToManyField(LAN, verbose_name=_(u'relevant LANs'), blank=True)
    pinned = models.BooleanField(_(u'pinned'), default=False, help_text=_(u'Pinned articles are shown before non-pinned ones.'))

    def count(self):
        return len(Article.objects.all())

    def get_absolute_url(self):
        return reverse('news_single', kwargs={'article_id': self.id})

    class Meta:
        verbose_name = _(u'news article')
        verbose_name_plural = _(u'news articles')
        ordering = ['-pub_date']
