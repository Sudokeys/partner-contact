# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas JEUDY <nicolas@sudokeys.com>
#    Copyright 2014-Today Sudokeys
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

from openerp import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('prospect')
    def _onchange_prospect(self):
        self.customer = not self.prospect

    @api.onchange('customer')
    def _onchange_customer(self):
        self.prospect = not self.customer

    prospect = fields.Boolean('Prospect')

    @api.multi
    def write(self, values):
        res = super(ResPartner, self).write(values)

        if values.get('prospect', 'none') != 'none' or values.get('customer', 'none') != 'none':
            for contact in self.child_ids:
                vals = {
                    'prospect': self.prospect,
                    'customer': self.customer,
                    'supplier': self.supplier,
                }
                contact.write(vals)
        return res
