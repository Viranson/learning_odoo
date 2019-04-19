# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School',
    'version': '1.1',
    'website': '',
    'category': 'New Module',
    'sequence': 10,
    'summary': 'This is a students module',
    'depends': [
        'base_setup'
    ],
    'description': "learning how to make a new module",
    'data': [
        "security/school.xml",
        "views/school_views.xml"
    ],
    'qweb': [],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
