# -*- coding: utf-8 -*-
{
'name': "My Library",  # Module title
    





    'name': "Estaciona",
    'summary': """
    Manage books easily""",  # Module subtitle phrase
    'description': """
    Este es un sistema integrado para la gestión de estacionamiento donde se puede reservar y alquilar parcelas para distinto tipode vehìculos
    """,

    'author': "Jorge Pluss",
    'website': "http://www.parkingapp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Application',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
    # Indicamos que es una aplicación
    'application':True,
}
