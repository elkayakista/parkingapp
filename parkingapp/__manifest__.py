# -*- coding: utf-8 -*-
{
    'name': "parkingapp",
    'summary': """ Sistema de Gestión de Playas de Estacionamientos """,  # Module subtitle phrase
    'description': """ Este es un sistema integrado para la gestión de estacionamiento donde se puede reservar y alquilar parcelas para distinto tipode vehìculos """,
    'author': "Jorge Pluss",
    'website': "http://www.parkingapp.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'application',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu_view.xml',
        'views/alquileres.xml',
        'security/parkingapp_security.xml',
        'security/ir.model.access.csv',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #'demo/demo.xml',
    #],
    'application':True,
}
