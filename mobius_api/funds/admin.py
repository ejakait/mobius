# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (FundHouse, FundCategory, FundScheme,
                     SchemePlan, AssetPortfolio)

# Register your models here.
admin.site.site_header = "Mobius"
admin.site.register(FundHouse)
admin.site.register(FundCategory)
admin.site.register(FundScheme)
admin.site.register(SchemePlan)
admin.site.register(AssetPortfolio)

