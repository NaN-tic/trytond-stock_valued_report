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
    'description': '''Report Stock Valued.
In Delivery Note Report, you can add group permisions:
- Stock
- Stock Price 
    ''',
    'description_ca_ES': '''Informe albarans valorats.
A la configuració del informe Albarà d'entrega', pot afegir els grups:
- Estoc
- Preus estoc
    ''',
    'description_es_ES': '''Informe albaranes valorados.
A la configuración del informe Albarán de entrega, puede añadir los grupos:
- Stock
- Precios stock
''',
    'depends': [
        'company',
        'stock_valued',
        ],
    'xml': [
        'shipment.xml',
        ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ],
}
