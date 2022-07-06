# -*- coding: utf-8 -*-
{
    'name': 'DiB - Account',
    'version': "1.0",
    'description': 
    """
    Este modulo contiene funciones para importar datos desde xlsx
    """,
    'author': 'ERP Siglo 21',
    'website': 'https://www.erpsiglo21.cl',
    'category': 'Accounting/Localizations/Account Charts',
    'depends': ['account'],
    'data': [
        "security/ir.model.access.csv",
        "wizards/dib_import_rrhh_accounts_wizard.xml",
        "views/account_move_views.xml"
        "reports/account_move_report.xml"
    ],
}