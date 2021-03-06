# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 Trustcode - www.trustcode.com.br                         #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp import fields, api, models


class res_partner(models.Model):
    _inherit = 'res.partner'

    ind_final = fields.Selection([
        ('0', u'Não'),
        ('1', u'Consumidor final')],
        string=u'Operação com Consumidor final', required=False,
        help=u'Indica operação com Consumidor final.', default='0')

    @api.onchange('is_company')
    def onchange_is_company(self):
        if self.is_company:
            self.ind_final = '0'
        else:
            self.ind_final = '1'
