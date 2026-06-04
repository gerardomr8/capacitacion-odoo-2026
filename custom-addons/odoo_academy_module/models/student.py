from odoo import models, fields

class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Academy Student'
    
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    birthdate = fields.Datetime(string='Birthdate')
    #enrollment_ids = fields.One2many('academy.enrollment', 'student_id', string='Enrollments')
    photo = fields.Binary(string='Photo')
    