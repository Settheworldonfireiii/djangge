# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from startup.models import Category, Good

admin.site.register(Category)

admin.site.register(Good)

# Register your models here.
