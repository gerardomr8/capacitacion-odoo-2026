from odoo import http
from odoo.http import request

class AcademyController(http.Controller):
    
    @http.route('/form-academy/school', auth='public', type='http', website=True)
    def index(self):
        return request.render('odoo_academy_module.formulario_estudiantes')
    
    @http.route('/registro/estudiantes', auth='public', type='http', website=True)
    def student_registration(self, **kwargs):
        if request.httprequest.method == 'POST':
            name = kwargs.get('name')
            lastname = kwargs.get('lastname')
            email = kwargs.get('email')
            birthdate = kwargs.get('birthdate')
            product_id = kwargs.get('product_id')
            school_id = kwargs.get('school')
            
            existing_student = request.env['academy.student'].sudo().search([('email', '=', email)], limit=1)
            
            if existing_student:
                return request.render('odoo_academy_module.error_registration')

            student_data = {
                'name': name,
                'last_name': lastname,
                'email': email,
                'birthdate': birthdate,
                'product': product_id,
                'school_id': int(school_id),
            }
            request.env['academy.student'].sudo().create(student_data)
            return request.render('odoo_academy_module.registration_success')