from odoo import models, fields

class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Academy Student'
    
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    birthdate = fields.Date(string='Birthdate')
    enrollment_ids = fields.One2many('academy.enrollment', 'student_id', string='Enrollments')
    photo = fields.Binary(string='Photo')