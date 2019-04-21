from odoo import api, fields, models



class students(models.Model):
    _name = "students.data"
    _description =  "this is a student data"
    
    name             = fields.Char(string = "Students name")
    # major            = fields.Char(string = "Major")
    students_number  = fields.Integer(string = "Students Number")
    mentor_id        = fields.Many2one("teachers.data", string = "Mentor")
    class_rooms      = fields.Many2many("class.room","students_data_rel","student_id","class_id", string ="Class")
    
class teacher(models.Model):
    _name = "teachers.data"
    name            = fields.Char(string = "Teachers Name")
    teachers_number = fields.Integer(string = "Teachers Number")
    students        = fields.One2many("students.data", "mentor_id", string = "Student ID")
    
class classroom(models.Model):
    _name = "class.room"
    name              = fields.Char(string = "Class")
    classroom_teacher = fields.Many2one(string = "Classroom Teacher")
    
    