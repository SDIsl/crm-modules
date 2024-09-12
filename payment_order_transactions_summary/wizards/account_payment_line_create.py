from odoo import api, fields, models


class AccountPaymentLineCreate(models.TransientModel):
    _inherit = 'account.payment.line.create'

    allow_normal = fields.Boolean(
        string='Allow Normal Move Lines',
        help='Allow normal move lines (No Blocked or Returned)'
    )

    @api.multi
    def _prepare_move_line_domain(self):
        domain = super(AccountPaymentLineCreate, self)._prepare_move_line_domain()
        if not self.allow_normal:
            domain += [
                '|',
                ('blocked', '=', True),
                ('invoice_id.returned_payment', '=', True)
            ]
        return domain
