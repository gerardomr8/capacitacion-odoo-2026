from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'
    
    student_read = fields.Boolean(string='Student Read Access', default=False)
    student_write = fields.Boolean(string='Student Write Access', default=False)
    student_create = fields.Boolean(string='Student Create Access', default=False)
    student_unlink = fields.Boolean(string='Student Unlink Access', default=False)
    
    ##TODO: Agregar permisos para los demas modelos (teacher, course, subject, director)