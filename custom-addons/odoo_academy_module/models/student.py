from odoo import models, fields, api
import logging

logger = logging.getLogger(__name__)

class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Academy Student'
    
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    birthdate = fields.Datetime(string='Birthdate')
    #enrollment_ids = fields.One2many('academy.enrollment', 'student_id', string='Enrollments')
    photo = fields.Binary(string='Photo')
    product = fields.Many2one('product.product', string='Product', ondelete='restrict', domain="[('type', '=', 'consu')]")
    curse_ids = fields.Many2many('academy.course', string='Courses')
    school_id = fields.Many2one('res.company', string='School', ondelete='restrict')
    
    @api.model_create_multi
    def create(self, vals_list):
        logger.info(self.env.user.company_id.id)        
        vals_list[0]['school_id'] = self.env.user.company_id.id
        partners = super().create(vals_list)
        logger.info("Creating students with the following data: %s", vals_list)
        logger.info("Students created: %s", partners)
        return partners
        