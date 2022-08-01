# -*- coding: utf-8 -*-

import datetime
import re

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_(u'user'), related_name='profile')
    nick = models.CharField(_(u'nick'), max_length=20, db_index=True, help_text=_(u'Your display name. Should be equal or similar to your username.'))
    date_of_birth = models.DateField(_(u'date of birth'), default=datetime.date.today)
    address = models.CharField(_(u'street address'), max_length=100)
    zip_code = models.CharField(_(u'postal code'), max_length=4)
    phone = models.CharField(_(u'phone number'), max_length=20)
    marketing_optin = models.BooleanField(_(u'marketing opt-in'), default=False, help_text=_(u'Receive emails about upcoming LANs and stuff.'))

    def __unicode__(self):
        return self.user.username

    def has_address(self):
        if self.address and self.zip_code:
            if not self.address.strip() or not self.zip_code.strip():
                return False
            return True
        return False

    class Meta:
        verbose_name = _(u'user profile')
        verbose_name_plural = _(u'user profiles')
        permissions = (
            ('show_private_info', u'Can show private user info'),
        )

    @staticmethod
    def check_username(username):
        if User.objects.filter(username=username).count() > 0:
            return ugettext(u'There is already a user with that username.')
        if not re.match('^[a-zA-Z0-9_-]+$', username):
            return ugettext(u'Your desired username contains illegal characters. Valid: a-Z 0-9 - _')
        return None

    @staticmethod
    def check_nick(nick):
        if not re.match('^[a-zA-Z0-9_-]+$', nick):
            return ugettext(u'Your desired nickname contains illegal characters. Valid: a-Z 0-9 - _')
        return None

    @staticmethod
    def check_date_of_birth(date_of_birth):
        now = datetime.date.today()
        if date_of_birth == now:
            return ugettext(u'You seem to have been born today, that doesn\'t seem right.')
        elif date_of_birth >= now:
            return ugettext(u'You seem to be from the future, that doesn\'t seem right.')
        elif date_of_birth < now.replace(year=(now.year - 150)):
            return ugettext(u'You seem to be over 150 years old, that doesn\'t seem right.')
        return None

    @staticmethod
    def check_zip_code(zip_code):
        if len(zip_code) != 4 or not zip_code.isdigit():
            return ugettext(u'The postal code must be a 4 digit number.')
        return None

    @staticmethod
    def check_phone(phone):
        if not re.match('^((\\+|00)[0-9]{2})?[0-9]{8,10}$', phone):
            return ugettext(u'The phone number must consist of an optional country code followed by 8–10 digits (no spaces or symbols, but "+" allowed in country code).')
        return None


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class AliasType(models.Model):
    description = models.CharField(_(u'description'), max_length=100)
    profile_url = models.URLField(_(u'profile URL'), blank=True, null=True, help_text=_(u'URL prefix where profile info can be '
                                  'retrieved. E.g. https://steamcommunity.com/id/'))
    activity = models.ManyToManyField('competition.Activity', verbose_name=_(u'activity'), related_name='alias_type')

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = _(u'user alias type')
        verbose_name_plural = _(u'user alias types')


class Alias(models.Model):
    alias_type = models.ForeignKey(AliasType, verbose_name=_(u'alias type'))
    nick = models.CharField(_(u'nickname'), max_length=40)
    user = models.ForeignKey(User, verbose_name=_(u'user'), related_name='alias')

    def __unicode__(self):
        return self.nick

    class Meta:
        verbose_name = _(u'user alias')
        verbose_name_plural = _(u'user aliases')
        unique_together = ('user', 'alias_type')
