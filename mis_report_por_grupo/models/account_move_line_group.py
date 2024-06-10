###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models, tools, api


class AccountMoveLineGroup(models.Model):
    _name = 'account.move.line.group'
    _description = 'Apuntes por Grupo de Cuentas'
    _auto = False
    _table = 'account_move_line_group'

    account_id = fields.Many2one('account.account', string='Account')
    date = fields.Date(string='Date')
    credit = fields.Float(string='Credit')
    debit = fields.Float(string='Debit')
    company_id = fields.Many2one('res.company', string='Company')
    user_type_id = fields.Many2one(
        'account.account.type',
        auto_join=True,
        readonly=True,
        index=True,
    )
    reconciled = fields.Boolean(
        readonly=True,
    )
    full_reconcile_id = fields.Many2one(
        'account.full.reconcile',
        string="Matching Number",
        readonly=True,
        index=True,
    )
    partner_id = fields.Many2one('res.partner', string='Partner')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW account_move_line_group AS (
                SELECT
                    acc2.id AS account_id,
                    acc2.code AS acc2_code,
                    acc2.name AS acc2_name,
                    acc.code AS original_code,
                    acc.name AS original_name,
                    aml.id AS id,
                    aml.date AS date,
                    aml.debit AS debit,
                    aml.credit AS credit,
                    aml.company_id AS company_id,
                    aml.user_type_id AS user_type_id,
                    aml.reconciled AS reconciled,
                    aml.full_reconcile_id AS full_reconcile_id,
                    aml.partner_id AS partner_id
                FROM account_move_line aml
                JOIN account_account acc ON aml.account_id = acc.id
                LEFT JOIN (
                    SELECT aa.group_id, aa.company_id, aa.id, aa.code, aa.name
                    FROM account_account aa
                    WHERE aa.code = (
                        SELECT MIN(code)
                        FROM account_account aa2
                        WHERE aa2.group_id = aa.group_id
                        AND aa2.company_id = aa.company_id
                    )
                    GROUP BY
                    aa.group_id, aa.company_id, aa.id, aa.code, aa.name
                ) AS acc2 ON acc2.group_id = acc.group_id
                AND acc2.company_id = aml.company_id
            )
        """)
        accounts = self.env['account.account']
        for acc in self.env['account.account'].search([
                ('user_type_id', '!=', 'Current Year Earnings'),
                ('group_id', '!=', False),]):
            if not accounts.search([
                    ('company_id', '=', acc.company_id.id),
                    ('code', '=', acc.group_id.code_prefix)]):
                acc.copy({
                    'company_id': acc.company_id.id,
                    'name': acc.group_id.name or '',
                    'code': acc.group_id.code_prefix,
                    'deprecated': True,
                    'asset_profile_id': False,
                })
