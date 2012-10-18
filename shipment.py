#This file is part stock_valued_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.modules.company import CompanyReport

__all__ = ['DeliveryValued']

class DeliveryValued(CompanyReport):
    'Stock Delivery Report Valued'
    __name__ = 'stock.shipment.out.delivery_valued'

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        localcontext['product_name'] = lambda product_id, language: \
                cls.product_name(product_id, language)
        return super(DeliveryValued, cls).parse(report, objects, data,
                localcontext)

    @classmethod
    def product_name(cls, product_id, language):
        Product = Pool().get('product.product')
        with Transaction().set_context(language=language):
            return Product(product_id).rec_name
