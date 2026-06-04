from odoo import models, fields

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    #tags_ids = fields.Many2many('academy.tag', string='Tags')
    student_ids = fields.Many2many('academy.student', string='Students')
    teacher_id = fields.Many2one('academy.teacher', string='Teacher', ondelete='restrict')