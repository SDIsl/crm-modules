###############################################################################
#
#    Copyright (C) 2024-Today SIDOO Soluciones SL
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
    'name': 'MIS Report por Grupo',
    'summary': 'Vista para sacar balances MIS por grupo en lugar de cuenta.',
    'author': 'Sergio Lop Sanz',
    'website': 'https://www.sidoo.es',
    'license': 'AGPL-3',
    'category': 'MIS Report',
    'version': '12.0.0',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
}