# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from funds.models import SchemePlan
from users.models import Info
# Create your models here.


class Transaction(models.Model):
    '''
    Saves each transaction's details for internal record
    Used to create records of TransactionBSE and TransactionXsipBSE
            that are sent to BSEStar's API endpoints
    '''

    # status of the transaction. most imp states are 1, 2 and 6 for bse
    STATUS = (
        ('0', 'Requested internally'),  # bse order not placed yet
        ('1', 'Cancelled/Failed- refer to status_comment for reason'),
        ('2', 'Order successfully placed at BSE'),
        ('4', 'Redirected after payment'),
        ('5', 'Payment provisionally made'),
        ('6', 'Order sucessfully completed at BSE'),
        ('7', 'Reversed'),  # when investment has been redeemed
        ('8', 'Concluded'),  # valid for SIP only when SIP completed/stopped
    )
    TRANSACTIONTYPE = (
        ('P', 'Purchase'),
        ('R', 'Redemption'),
        ('A', 'Additional Purchase'),
    )

    user = models.ForeignKey(Info,
                             on_delete=models.PROTECT,
                             related_name='transactions',
                             related_query_name='transaction')
    scheme_plan = models.ForeignKey(SchemePlan,
                                    on_delete=models.PROTECT,
                                    related_name='transactions',
                                    related_query_name='transaction')

    transaction_type = models.CharField(
        max_length=1, blank=False, choices=TRANSACTIONTYPE, default='P')  # purchase redemption etc

    # track status of transaction and comments if any from bse or rta
    status = models.CharField(max_length=1, choices=STATUS, default='0')
    status_comment = models.CharField(max_length=1000, blank=True)

    amount = models.FloatField(validators=[MinValueValidator(
        0), MaxValueValidator(1000000)], blank=True, null=True)
