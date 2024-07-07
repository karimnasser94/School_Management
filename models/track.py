from odoo import models, fields


class Track(models.Model):
    _name = 'iti.track'
    _description = 'Track'

    name = fields.Char()
    branch = fields.Char()
    info = fields.Text()
    description = fields.Html()
    capacity = fields.Integer()
    start_date = fields.Date()
    duration = fields.Float()
    is_open = fields.Boolean()
    student_ids = fields.One2many('iti.student', 'track_id')
