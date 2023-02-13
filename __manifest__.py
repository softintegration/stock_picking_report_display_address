# -*- coding: utf-8 -*- 


{
    'name': 'Display source and destination address in Internal pickings report',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Stock',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'report/report_deliveryslip.xml',
        'views/stock_picking_views.xml'
    ],
    'license': 'LGPL-3',
}
