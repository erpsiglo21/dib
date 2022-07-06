# -*- coding: utf-8 -*-
{
    'name': 'DiB - Stock',
    'version': "1.0",
    'description': 
    """
    Este modulo contiene las extensiones a inventarios
    """,
    'author': 'ERP Siglo 21',
    'website': 'https://www.erpsiglo21.cl',
    'category': 'Accounting/Localizations/Account Charts',
    'depends': ['product','stock','sale_stock','stock_account'],
    'data': [
        'views/stock_move_rotulate_view.xml',
        'views/stock_valuation_layer_custom.xml'
    ],
}
