# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser)
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.encoding import smart_unicode


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    site = models.CharField(max_length=1000, verbose_name='Сайт', blank=True, null=True)
    address = models.CharField(max_length=500, verbose_name='Адрес', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', blank=True, null=True,
                                 related_name='company_category')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    image = models.ImageField(upload_to='images/user_images', verbose_name='Аватар', blank=True, null=True)

    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона', blank=True, null=True)

    company_status = models.BooleanField(default=False, verbose_name='Статус пользователя')
    company = models.ForeignKey(Company, verbose_name='Компания', blank=True, null=True, related_name='user_company')

    # REQUIRED_FIELDS = []
    # USERNAME_FIELD = 'username'

    def __unicode__(self):
        return smart_unicode(self.username)
