{
    'name': "Odoo Academy Module",
    'version': "19.0.0",
    'author': "Quadit SA de CV",
    'website': "https://www.quadit.mx",
    'summary': "A module for managing an academy in Odoo",
    'description': "This module allows you to manage courses, students, and enrollments in an academy setting.",
    'depends': ["base", "product"],
    'license': 'LGPL-3', 
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/rules_student.xml',
    ],
    'installable': True,
    'application': True,
}