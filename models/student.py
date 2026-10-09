from odoo import models, fields

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Student Name', required=True)
    roll_number = fields.Char(string='Roll Number', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    course = fields.Char(string='Course')
    admission_date = fields.Date(string='Admission Date', default=fields.Date.today)
    age =fields.Integer(string='age')
    date_of_birth = fields.Date(string='Date of Birth')
    active = fields.Boolean(default=True)

class StudentCourse(models.Model):
    _name = 'student.course'
    _description = 'Student Course'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code')
    duration = fields.Integer(string='Duration in Years')


class StudentDepartment(models.Model):
    _name='student.department'
    _description = 'Student Department'

    name=fields.Char(string='Department Name',required=True)
    course=fields.Char(string='Course')
    roll_number=fields.Char(string='Roll Number',reuired=True)