# -*- coding: utf-8 -*-

{
    'name': 'Multiple Invoice Payment',
    'category': 'Accounting',
    'summary': 'Validate one payment against multiple invoices of a partner.',
    'version': '1.0',
    'description': """""",
    'author': "Nirmay 89",
    'website': "https://apps.odoo.com/apps/modules/browse?author=Nirmay%2089",
    'license': "OPL-1",
    'price': "10",
    'currency': 'EUR',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_payment_view.xml'
    ],
    'images':['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': True,
}
