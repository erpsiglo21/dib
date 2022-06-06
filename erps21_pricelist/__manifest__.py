# -*- coding: utf-8 -*-
{
    'name': "ERPSiglo21 Pricelist",

    'summary': """
        Permite la carga masiva de listas de precio
        """,

    'description': """
Permite la carga masiva de listas de precio a partir de un archivo Excel.
Las columnas del archivo son las siguiente:
    - Nombre de la lista de precio (De no existir se creará una nueva)
    - SKU
    - Precio
    """,

    'author': "ERP Siglo 21",
    'website': "http://erpsliglo21.cl",

    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],
    'external_dependencies': {
        'python': [
            'base64',
            'xlrd',
        ]
    },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/erps21_pricelist_upload.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
