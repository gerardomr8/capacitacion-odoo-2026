from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    filter_example = fields.Char(string='Filter Example')