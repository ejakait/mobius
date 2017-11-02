# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class FundHouse(models.Model):

    # key details
    amc_code = models.CharField(
        max_length=3, blank=False, verbose_name='AMC Code')
    name = models.CharField(max_length=100, unique=True)
    launch_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    total_aum = models.FloatField(blank=True, null=True)

    # metadata
    address = models.CharField(max_length=500, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    website = models.URLField(max_length=50, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    fax = models.CharField(max_length=100, blank=True)


class FundCategory(models.Model):
    '''
    Stores mutual fund category details. you can classify funds as you like
    Like liquid, debt, large cap equity, small cap equity, tax saver (jargon: ELSS), etc
    '''
    name = models.CharField(max_length=100, unique=True, blank=True)
    num_funds = models.IntegerField(null=True)


class FundScheme(models.Model):
    '''
    Stores a mutual fund's details
    Like Mirae Asset Emerging Bluechip Fund, Axis Long Term Equity etc
    '''
    name = models.CharField(max_length=100, unique=True)
    fund_category = models.ForeignKey(
        FundCategory, on_delete=models.PROTECT, blank=True, null=True, related_name='fund_category_list')
    fund_house = models.ForeignKey(
        FundHouse, on_delete=models.PROTECT, blank=True, null=True, related_name='fund_house_list')

    # key details
    objective = models.CharField(max_length=1000, blank=True)
    aum = models.FloatField(blank=True, null=True)  # in Rs cr
    aum_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)


class SchemePlan(models.Model):
    '''
    Stores the details of a scheme. every FundScheme has multiple SchemePlans
    Like Mirae Asset Emerging Bluechip Fund Direct Growth, Mirae Asset Emerging Bluechip Fund Direct Dividend, 
        Mirae Asset Emerging Bluechip Fund Regular Growth, Mirae Asset Emerging Bluechip Fund Regular Dividend etc
    '''
    name = models.CharField(max_length=100, unique=True)
    fund_scheme = models.ForeignKey(
        FundScheme, on_delete=models.PROTECT, null=True, related_name="scheme_plan_list")

    # imp codes for doing transaction
    bse_code = models.CharField(max_length=15, blank=True)
    rta_code = models.CharField(max_length=10, blank=True)
    amc_code = models.CharField(max_length=10, blank=True)
    isin = models.CharField(max_length=15, blank=True)

    # schemeplan type; figured out by parsing name of SchemePlan
    # regular, growth is most commonly transacted
    # set true if 'direct' in name; false means regular
    if_direct = models.NullBooleanField(default=False, null=True)
    # set false for dividend i.e. if 'dividend' in name but 'dividend yield' not in name
    if_growth = models.NullBooleanField(default=False, null=True)
    if_open = models.NullBooleanField(default=True, null=True)

    # key details
    launch_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    # stale data- of direct plan  # in Rs cr
    asset_size = models.FloatField(blank=True, null=True)
    asset_size_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    expense_ratio = models.FloatField(validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)  # in %
    expense_ratio_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    nav_latest = models.FloatField(blank=True, null=True)
    nav_latest_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    # dividend details
    dividend_history = models.CharField(max_length=1000, blank=True)


class AssetPortfolio(models.Model):
    '''
    Stores overall portoflio details for a fund scheme or benchmark index or fund category. 
    in every row, any one foreign key is filled while the other two are empty
    '''
    fund_scheme = models.ForeignKey(
        FundScheme, on_delete=models.PROTECT, blank=True, null=True)
    fund_category = models.ForeignKey(
        FundCategory, on_delete=models.PROTECT, blank=True, null=True)

    # composition of portfolio
    num_assets = models.IntegerField(
        validators=[MinValueValidator(0)], blank=True, null=True)
    debt_pc = models.FloatField(default=0)
    equity_pc = models.FloatField(default=0)
    cash_pc = models.FloatField(default=0)
    other_pc = models.FloatField(default=0)
