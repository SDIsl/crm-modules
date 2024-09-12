###############################################################################
#
#    SDi Soluciones Informáticas
#    Copyright (C) 2021-Today SDi Soluciones Informáticas <www.sdi.es>
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
###############################################################################
{
    'name': 'Summary of transactions at payment order form',
    'summary': 'Count and .',
    'category': 'payment',
    'version': '12.0.0.0.210308',
    'author': 'Sergio Lop Sanz, SDi Soluciones Informáticas',
    'website': 'https://www.sdi.es/odoo-cloud/',
    'license': 'AGPL-3',
    'depends': [
        'account_payment_order',
    ],
    'data': [
        'views/account_payment_order_views.xml',
        'wizards/account_payment_line_create_view.xml',
        'report/print_account_payment_order_document.xml',
    ],
}
