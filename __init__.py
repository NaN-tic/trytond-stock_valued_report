#This file is part stock_valued_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *


def register():
    Pool.register(
        DeliveryValued,
        module='stock_valued_report', type_='report')
