# Copyright 2014-2018 Tecnativa - Pedro M. Baeza
# Copyright 2015 Antonio Espinosa - Tecnativa <antonio.espinosa@tecnativa.com>
# Copyright 2018 Luis M. Ontalba - Tecnativa <luis.martinez@tecnativa.com>
# Copyright 2016-2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_line = fields.Many2one(
        related='move_id.sale_line_id', readonly=True,
        string='Related order line',
        related_sudo=True,  # See explanation for sudo in compute method
    )
    currency_id = fields.Many2one(
        related='sale_line.currency_id', readonly=True,
        string='Sale Currency',
        related_sudo=True,
    )
    sale_tax_id = fields.Many2many(
        related='sale_line.tax_id', readonly=True,
        string='Sale Tax',
        related_sudo=True,
    )
    sale_price_unit = fields.Float(
        string='Sale price unit',
        digits=dp.get_precision('Product Price'),
        compute='_compute_sale_order_line_fields',
    )
    sale_discount = fields.Float(
        related='sale_line.discount', readonly=True,
        string='Sale discount (%)',
        related_sudo=True,
    )
    sale_tax_description = fields.Char(
        compute='_compute_sale_order_line_fields',
        string='Tax Description',
        compute_sudo=True,  # See explanation for sudo in compute method
    )
    sale_price_subtotal = fields.Monetary(
        compute='_compute_sale_order_line_fields',
        string='Price subtotal',
        compute_sudo=True,
    )
    sale_price_tax = fields.Float(
        compute='_compute_sale_order_line_fields',
        string='Taxes',
        compute_sudo=True,
    )
    sale_price_total = fields.Monetary(
        compute='_compute_sale_order_line_fields',
        string='Total',
        compute_sudo=True,
    )

    discount = fields.Float(
        string='Precio por unidad',
        related="move_id.sale_line_id.discount",
        related_sudo=True,
    )

    # sale_line.price_unit * sale_line.product_uom.factor
    def _calculate_price_unit(self):
        return self.sale_line.price_unit

    def _calculate_units(self):
        return self.sale_line.qty_done

    @api.multi
    def _compute_sale_order_line_fields(self):
        for line in self:
            sale_line = line.sale_line
            line.sale_price_unit = line._calculate_price_unit()
            units = line._calculate_units()
            # price_unit = (
            #     sale_line.price_subtotal / sale_line.product_uom_qty
            #     if sale_line.product_uom_qty else sale_line.price_reduce)
            price_unit = \
                line.sale_price_unit - line.sale_price_unit * \
                line.discount / 100
            taxes = line.sale_tax_id.compute_all(
                price_unit=price_unit,
                currency=line.currency_id,
                quantity=units or line.product_qty,
                product=line.product_id,
                partner=sale_line.order_id.partner_shipping_id)
            if sale_line.company_id.tax_calculation_rounding_method == (
                    'round_globally'):
                price_tax = sum(
                    t.get('amount', 0.0) for t in taxes.get('taxes', []))
            else:
                price_tax = taxes['total_included'] - taxes['total_excluded']
            line.update({
                'sale_tax_description': ', '.join(
                    t.name or t.description for t in line.sale_tax_id),
                'sale_price_subtotal': taxes['total_excluded'],
                'sale_price_tax': price_tax,
                'sale_price_total': taxes['total_included'],
            })
