###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    disable_vat_check = fields.Boolean(
        string="Disable VAT validation",
        config_parameter="partner_disable_vat_check_option.disable_vat_check",
    )
