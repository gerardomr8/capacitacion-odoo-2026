from odoo import models, fields

class AcademyDirector(models.Model):
    _name = 'academy.director'
    _description = 'Academy Director'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    birthdate = fields.Datetime(string='Birthdate')
    photo = fields.Binary(string='Photo')
    school_id = fields.Many2one('res.company', string='School', ondelete='restrict')
    teacher_ids = fields.One2many('academy.teacher', 'director_id', string='Teachers')