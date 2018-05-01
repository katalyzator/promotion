# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from main.models import *


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', ]
    list_display = ['username', 'email']


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Company)
