###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models, tools


class AccountGlobalBalance(models.Model):
    _name = 'account.global.balance'
    _description = 'Apuntes con acumulado global mensual'
    _auto = False
    _table = 'account_global_balance'

    id = fields.Integer(string='ID', readonly=True)
    account_id = fields.Many2one('account.account', string='Account')
    month = fields.Date(string='Month')
    balance = fields.Float(string='Balance', group_operator='avg')

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW account_global_balance AS (
                WITH monthly_balance AS (
                    SELECT
                        account_id,
                        DATE_TRUNC('MONTH', date) AS month,
                        SUM(debit) - SUM(credit) AS balance
                    FROM
                        account_move_line
                    WHERE
                        parent_state = 'posted'
                    GROUP BY
                        account_id,
                        DATE_TRUNC('MONTH', date)
                ),
                cumulative_balance AS (
                    SELECT
                        account_id,
                        month,
                        SUM(balance) OVER (
                            PARTITION BY account_id
                            ORDER BY month
                            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                        ) AS balance
                    FROM
                        monthly_balance
                ),
                numbered_balance AS (
                    SELECT
                        ROW_NUMBER() OVER (ORDER BY account_id, month) AS id,
                        *
                    FROM
                        cumulative_balance
                )
                SELECT * FROM numbered_balance
            );
        """)
