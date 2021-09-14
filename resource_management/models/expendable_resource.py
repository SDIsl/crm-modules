###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, api, fields, models


class ExpendableResource(models.Model):
    _name = 'resource.expendable'
    _description = 'Expendable resource of an employee.'

    name = fields.Char(
        string='Name',
        required=True,
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
    )
    delivery_date = fields.Date(
        string='Delivery Date',
        default=lambda self: fields.Date.context_today(self),
    )
    description = fields.Text(
        string="Description",
    )

    @api.multi
    def write(self, vals):
        for resource in self:
            msg = _('<p>Changes in Expendable Resource '
                    '<strong>{resource}</strong>:</br>').format(
                resource=resource.name,
            )
            post = False
            if 'name' in vals and vals.get(
               'name') != resource.name:
                msg += _('<li><strong>Name:</strong> {old_val} '
                         '<span class="fa fa-long-arrow-right"'
                         ' title="Changed"/> {new_val}</li>').format(
                    old_val=resource.name,
                    new_val=vals['name'],
                )
                post = True
            if 'description' in vals and vals.get(
               'description') != resource.description:
                msg += _('<li><strong>Description:</strong> {old_val} '
                         '<span class="fa fa-long-arrow-right"'
                         ' title="Changed"/> {new_val}</li>').format(
                    old_val=resource.description,
                    new_val=vals['description'],
                )
                post = True
            msg += '</p>'
            if post:
                resource.employee_id.message_post(body=msg)
        return super().write(vals)

    @api.multi
    def unlink(self):
        for resource in self:
            msg = _('<p>An Expendable Resource was deleted:</p>'
                    '<li><strong>Name: </strong>{resource}</li>'
                    '<li><strong>Delivery Date: </strong>{delivery_date}</li>'
                    '<li><strong>Description: </strong>{description}</li>'
                    ).format(
                resource=resource.name, delivery_date=resource.delivery_date,
                description=resource.description
            )
            resource.employee_id.message_post(body=msg)
        return super().unlink()