# -*- coding: utf-8 -*-
{
    'name': "Valores por defecto facturación",

    'summary': """
        Se agregan los campos forma de pago y uso a la ficha del cliente, estos valores
        son llenados de manera automática en la factura""",

    'description': """
        El objetivo de este módulo es que el usuario establesca la forma de pago y uso de la factura desde la ficha del cliente. 
        Al momento de hacer la factura el sistema tomará estos valores según el cliente seleccionado
    """,

    'author': "Juan Paulo Rodriguez",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contabilidad',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','account','l10n_mx_edi'],

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
