# -*- coding: utf-8 -*-
{
    'name': 'DiB - Maestros',
    'version': "1.0",
    'description': 
    """
    Este modulo contiene las extensiones a los maestros
    """,
    'author': 'ERP Siglo 21',
    'website': 'https://www.erpsiglo21.cl',
    'category': 'Accounting/Localizations/Account Charts',
    'depends': ['product','stock','l10n_cl_edi'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/product_segment_views.xml",
        "views/product_template_views.xml",
        "views/res_partner_views.xml",
    ],
}
