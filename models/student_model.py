from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class StudentModel(models.Model):
    _name = 'iti.student'

    name = fields.Char()
    email = fields.Char(string="Email")
    age = fields.Integer(string="Age")
    info = fields.Text()
    salary = fields.Float()
    birthdate = fields.Date()
    interview_time = fields.Datetime()
    description = fields.Html()
    is_accepted = fields.Boolean()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ])
    avatar = fields.Image()
    track_id = fields.Many2one('iti.track', string='My Track')
    branch = fields.Char(related='track_id.branch')
    skills_ids = fields.Many2many('iti.skill')
    state = fields.Selection([
        ('new', 'New'),
        ('interviewing', 'Interviewing'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='new')

    computed_age = fields.Integer(compute='compute_student_age')

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Name Already Exist'),
        ('check_salary', 'CHECK(salary > 0)', 'Salary must be greater than 0'),
    ]

    @api.depends('birthdate')
    def compute_student_age(self):
        for rec in self:
            if rec.birthdate:
                rec.computed_age = datetime.now().year - rec.birthdate.year
            else:
                rec.computed_age = 0

    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        if self.birthdate:
            self.age = datetime.now().year - self.birthdate.year
            return {
                'warning': {
                    'title': "Age Change",
                    'message': "Age has been changed"
                }
            }

    def set_to_interviewing(self):
        self.state = 'interviewing'

    def set_to_accepted(self):
        self.state = 'accepted'

    def set_to_rejected(self):
        self.state = 'rejected'

    def set_to_new(self):
        self.state = 'new'

    @api.constrains('email')
    def check_email_address(self):
        for rec in self:
            if '@' not in rec.email:
                raise ValidationError('Please insert a Valid Mail Ya 7ooby')
        # for rec in self:
        #     if '@' not in rec.email:
        #         raise ValidationError('Please insert a Valid Mail Yastaaa')

    @api.model
    def create(self, vals):
        if '@' not in vals['email']:
            vals['email'] += '@gmail.com'
        return super().create(vals)
    
    def write(self, vals):
        if vals.get('email') and '@' not in vals['email']:
            vals['email'] += '@gmail.com'
        return super().write(vals)


