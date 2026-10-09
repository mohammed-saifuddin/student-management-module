{
    'name': 'Student Management',
    'version': '1.0.0',
    'summary': 'Manage student records',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}