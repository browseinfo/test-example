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

from osv import fields, osv

class account_partner_ledger(osv.osv_memory):
    """
    This wizard will provide the partner Ledger report by periods, between any two dates.
    """
    _inherit = 'account.partner.ledger'
    _description = 'Account Partner Ledger'

    _columns = {
        'partner_ids': fields.many2many('res.partner', 'res_partner_ledger_rel', 'account_id', 'partner_id', 'Partners'),
    }
    
    def _print_report(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}
        res = super(account_partner_ledger, self)._print_report(cr, uid, ids, data, context=context)
        res['datas']['form'].update(self.read(cr, uid, ids, ['partner_ids'])[0])
        if data['form']['page_split']:
            return {
                'type': 'ir.actions.report.xml',
                'report_name': 'account.partner.ledger_partners',
                'datas': data,
        }
        return {
                'type': 'ir.actions.report.xml',
                'report_name': 'account.partner.ledger_other_partners',
                'datas': data,
        }
       
account_partner_ledger()
