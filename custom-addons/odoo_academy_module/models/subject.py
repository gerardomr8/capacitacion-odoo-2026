from odoo import models, fields

class AcademySubject(models.Model):
    _name = 'academy.subject'
    _description = 'Academy Subject'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one('academy.teacher', string='Teacher', ondelete='restrict')
    