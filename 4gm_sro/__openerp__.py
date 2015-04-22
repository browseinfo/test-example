# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Customization and bug fixes for SRO",
    "version" : "1.1",
    "author" : "OpenERP SA",
    "category": '',
    "sequence": 10,
    'complexity': "normal",
    "description": """
    """,
    'website': 'http://www.openerp.com',
    'init_xml': [],
    "depends" : ["geniusmind", "account_cancel", "crm"],
    'update_xml': [
        "sale_view.xml",
        "invoice_merge.xml",
        "wizard/base_partner_merge_view.xml",
        "wizard/invoice_merge_view.xml",
        "wizard/wizard_account_partner_ledger_view.xml",
        "account_partner_ledger_report.xml",
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
