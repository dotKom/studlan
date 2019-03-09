# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Key(models.Model):
    content = models.CharField('key', max_length=32, editable=False)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return u'API key for {0}'.format(self.owner)
