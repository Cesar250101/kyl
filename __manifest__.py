# -*- coding: utf-8 -*-
{
    'name': "kyl",

    'summary': """
                Localización empresa KYL, se agregar lo siguiente:
                1.- Coductor en las notas de ventas
                2.- Se integra las facturas de compras con el módulo de control de Flota""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Method",
    'website': "http://www.openmethod.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','fleet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}