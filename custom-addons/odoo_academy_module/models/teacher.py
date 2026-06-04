from odoo import models, fields

class AcademyTeacher(models.Model):
    _name = 'academy.teacher'
    _description = 'Academy Teacher'
    
    name = fields.Char(string='Name', required=True)
    biography = fields.Html(string='Biography')
    active = fields.Boolean(string='Active', default=True)
    subjects_ids = fields.One2many('academy.subject', 'teacher_id', string='Subjects')
    photo = fields.Binary(string='Photo')
    
    
    