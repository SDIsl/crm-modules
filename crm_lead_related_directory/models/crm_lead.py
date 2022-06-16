###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    related_directory_id = fields.Many2one(
        string='Related Directory',
        comodel_name='dms.directory',
        copy=False,
    )

    def create_directory(self):
        parent_directory = self.env['dms.directory'].\
            search([('name', '=', 'Leads')])
        admin_group = self.env['dms.access.group'].\
            search([('name', '=', 'Admin')])

        if self.env['dms.directory'].search([('name', '=', self.name)]):
            raise UserError(
                _('Directory with this name already exists.\n'
                    'If you really want to create a directory related with '
                    'this lead, you should change its name.')
            )
        else:
            directory = self.env['dms.directory'].create(vals_list={
                'name': self.name,
                'is_root_directory': False,
                'parent_id': parent_directory.id,
                'is_hidden': False,
                'complete_group_ids': [(4, admin_group.id)],
                'related_lead_id': self.id,
            })

        self.related_directory_id = directory
        self.message_post(body=_('Directory related has been created'))

    def related_directory_link(self):
        return {
            'res_model': 'dms.directory',
            'res_id': self.related_directory_id.id,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('dms.view_dms_directory_form').id,
            'target': 'self',
        }
