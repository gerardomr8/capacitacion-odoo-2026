{
    'name': "Odoo Academy Module",
    'version': "19.0.0",
    'author': "Quadit SA de CV",
    'website': "https://www.quadit.mx",
    'category': 'Education',
    'summary': "A module for managing an academy in Odoo",
    'description': "This module allows you to manage courses, students, and enrollments in an academy setting.",
    'depends': ["base", "product"],
    'license': 'LGPL-3', 
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        
        'views/student_view.xml',
        'views/rules_student.xml',
        'views/course_view.xml',
        'views/teacher_view.xml',
        'views/subject_view.xml',
        'views/director_view.xml',
        
        'template/template_student.xml',
        'template/template_success.xml',
        'template/template_error.xml',
    ],
    'installable': True,
    'application': True,
}