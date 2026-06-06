from odoo import models, fields, api

class AcademyTeacher(models.Model):
    _name = 'academy.teacher'
    _description = 'Academy Teacher'
    
    name = fields.Char(string='Name', required=True)
    biography = fields.Html(string='Biography')
    active = fields.Boolean(string='Active', default=True)
    subjects_ids = fields.One2many('academy.subject', 'teacher_id', string='Subjects')
    photo = fields.Binary(string='Photo')
    school_id = fields.Many2one('res.company', string='School', ondelete='restrict')
    director_id = fields.Many2one('academy.director', string='Director', ondelete='restrict')
    curse_ids = fields.Many2many('academy.course', 'teacher_id', string='Courses')
    
    @api.model_create_multi
    def create(self, vals_list):
        vals_list[0]['school_id'] = self.env.user.company_id.id
        partners = super().create(vals_list)
        return partners
    
    
    