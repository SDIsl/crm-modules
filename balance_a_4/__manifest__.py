###############################################################################
#
#    SDi Soluciones Informáticas
#    Copyright (C) 2020-Today SDi Soluciones Informáticas <www.sdi.es>
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
    'name': 'Balances MIS a 4',
    'summary': 'Balance MIS a 4',
    'author': 'Sergio Lop, SDi Soluciones Informáticas',
    'website': 'https://sdi.es/odoo/',
    'license': 'AGPL-3',
    'category': 'Invocie',
    'version': '12.0.1.0.0',
    'depends': [
        'l10n_es_mis_report',
    ],
    'data': [
        'data/mis_report_pyg_a_4.xml',
    ],
}
