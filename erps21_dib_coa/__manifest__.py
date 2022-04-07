# -*- coding: utf-8 -*-
{
    'name': 'DiB - Accounting',
    'version': "1.0",
    'description': """
DiB accounting chart and tax localization.
Plan contable de empresas DiB e impuestos de acuerdo a disposiciones vigentes
    """,
    'author': 'ERP Siglo 21',
    'website': 'https://www.erpsiglo21.cl',
    'category': 'Accounting/Localizations/Account Charts',
    'depends': ['account', 'l10n_cl'],
    'data': [
        'data/chart_template.xml',
        'data/account.account.template.csv',
        'data/chart_template_update.xml',
        'data/tax_template_comercial.xml',
        'data/fiscal_template_comercial.xml',
        'data/chart_template_load.xml',
    ],
}
