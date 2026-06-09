from ast import Raise
from odoo import models, fields, api
import logging
from odoo.exceptions import AccessError

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
    course_ids = fields.Many2many('academy.course', string='Courses')
    school_id = fields.Many2one('res.company', string='School', ondelete='restrict')
    
    @api.model_create_multi
    def create(self, vals_list):
        """Aplicaremos una condicion de escritura basada en el campo student_create del modelo res.users"""
        if not self.env.user.student_create:
            logger.warning("No tienes permisos para crear estudiantes.")
            raise AccessError("No tienes permisos para crear estudiantes.")
        vals_list[0]['school_id'] = self.env.user.company_id.id
        partners = super().create(vals_list)
        return partners
    
    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, **kwargs):
        """Aplicaremos una condicion de lectura basada en el campo student_read del modelo res.users"""
        if not self.env.user.student_read:
            logger.warning("No tienes permisos para leer estudiantes.")
            return super()._search([('id', '=', False)], offset=offset, limit=limit, order=order, **kwargs)
        
        return super()._search(domain, offset=offset, limit=limit, order=order, **kwargs)
    
    def write(self, vals):
        """Aplicaremos una condicion de modificacion basada en el campo student_write del modelo res.users"""
        if not self.env.user.student_write:
            logger.warning("No tienes permisos para modificar estudiantes.")
            raise AccessError("No tienes permisos para modificar estudiantes.")
        return super().write(vals)
    
    def unlink(self):
        """Aplicaremos una condicion de eliminacion basada en el campo student_unlink del modelo res.users"""
        if not self.env.user.student_unlink:
            logger.warning("No tienes permisos para eliminar estudiantes.")
            raise AccessError("No tienes permisos para eliminar estudiantes.")
        return super().unlink()