# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software.
# mail:   odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software.
# Contributions:
#           Aktiv Software:
#              - Juhi Upadhyay
#              - Nupur Soni
#              - Dharmesh Jagatiya
#              - Saurabh Yadav
{
    'name': "Unreserved Components in MRP Orders",
    'summary': """
            This Module is used to unreserve Raw Materials in the MRP. """,
    'description': """
        This Module is use to Unreserve Specific Raw Material in the MRP
    """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'license': "AGPL-3",
    'version': '14.0.1.0.0',
    'depends': ['mrp'],
    'data': [
        'views/mrp_production_view.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'auto_install': False,
    'installable': True,
    'application': False
 
}
