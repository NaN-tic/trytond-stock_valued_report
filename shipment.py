#This file is part stock_valued_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.modules.company import CompanyReport

class DeliveryValued(CompanyReport):
    _name = 'stock.shipment.out.delivery_valued'

    def parse(self, report, objects, datas, localcontext):
        localcontext['product_name'] = lambda product_id, language: \
                self.product_name(product_id, language)
        return super(DeliveryValued, self).parse(report, objects, datas,
                localcontext)

    def product_name(self, product_id, language):
        product_obj = Pool().get('product.product')
        with Transaction().set_context(language=language):
            return product_obj.browse(product_id).rec_name

DeliveryValued()
