#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Stock Valued Report',
    'name_ca_ES': 'Informe alabarans valorats',
    'name_es_ES': 'Informe albaranes valorados',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Report Stock Valued''',
    'description_ca_ES': '''Informe albarans valorats''',
    'description_es_ES': '''Informe albaranes valorados''',
    'depends': [
        'stock_valued',
        ],
    'xml': [
        'shipment.xml',
        ],
    'translation': [
        # 'locale/ca_ES.po',
        # 'locale/es_ES.po',
    ],
}
