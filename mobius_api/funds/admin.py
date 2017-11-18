# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import auth
from transactions.models import Transaction
from rest_framework.authtoken.models import Token
from .models import (FundHouse, FundCategory, FundScheme,
                     SchemePlan, AssetPortfolio)


# Register your models here.
admin.site.site_header = "Z-CASH"
admin.site.register(FundHouse)
admin.site.register(FundCategory)
admin.site.register(FundScheme)
admin.site.register(SchemePlan)
admin.site.register(AssetPortfolio)
admin.site.register(Transaction)
admin.site.unregister(auth.models.Group)
admin.site.unregister(Token)

