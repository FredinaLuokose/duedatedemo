from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    due_date = fields.Date(string='Due Date')
