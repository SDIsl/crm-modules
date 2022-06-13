###############################################################################
#
#    SDi Soluciones Digitales
#    Copyright (C) 2022-Today SDi Soluciones Digitales <www.sdi.es>
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
    'name': 'Sale Management Template Search',
    'summary': 'Adds new fields to search for',
    'author': 'Darío Sanz, SDi Soluciones Digitales',
    'website': 'https://sdi.es/odoo/',
    'license': 'AGPL-3',
    'category': 'Sales',
    'version': '12.0.1.0.0',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/sale_order_template_views.xml',
    ],
}
