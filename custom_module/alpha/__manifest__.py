# -*- coding: utf-8 -*-
{
    'name': "alpha",
    'summary': """
        Test module""",
    'description': """
        For alpha club
    """,
    'author': "Alan Jimenez",
    'website': "https://alandevweb.com/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
