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

from report import report_sxw
from account.report.account_partner_ledger import third_party_ledger

class third_party_ledger_report(third_party_ledger):
    _name = 'report.account.partner.ledger_partners'

    def set_context(self, objects, data, ids, report_type=None):
        obj_partner = self.pool.get('res.partner')
        self.partner_ids = data['form'].get('partner_ids', False)
        new_ids = []
        if (data['model'] == 'res.partner'):
            new_ids = ids
            print "New........", new_ids
            objects = obj_partner.browse(self.cr, self.uid, new_ids)
            return super(third_party_ledger_report, self).set_context(objects, data, new_ids, report_type=report_type)
        data.update({'model': 'res.partner'})
        if self.partner_ids:
            new_ids = self.partner_ids
        objects = obj_partner.browse(self.cr, self.uid, new_ids)
        return super(third_party_ledger_report, self).set_context(objects, data, new_ids, report_type=report_type)

report_sxw.report_sxw('report.account.partner.ledger_partners', 'res.partner', 'addons/account/report/account_partner_ledger.rml',parser=third_party_ledger_report, header='internal')
report_sxw.report_sxw('report.account.partner.ledger_other_partners', 'res.partner', 'addons/account/report/account_partner_ledger_other.rml',parser=third_party_ledger_report, header='internal')
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
