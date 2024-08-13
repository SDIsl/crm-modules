###############################################################################
#
#    Sidoo, S.L.
#    Copyright (C) 2024-Today Sidoo, S.L. https://www.sdi.es/odoo-cloud/
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
    'name': 'SDi Grouped by Picking',
    'version': '11.0.1.0.0',
    'summary': 'Grouped by picking customization',
    'author': 'Valentín Georigan Castravete, Sidoo, S.L.',
    'website': 'https://www.sdi.es/odoo-cloud/',
    'license': 'AGPL-3',
    'category': 'Custom',
    'depends': [
        'sdi_sale_pack_uom_management_nocompute',
        'account_invoice_report_grouped_by_picking',
    ],
    'data': [
        'report/account_reports.xml',
    ],
}
