from odoo import fields, models


class TrackWizard(models.TransientModel):
    _name = 'iti.track.wizard'

    name = fields.Char()
    description = fields.Text()

    def save_track_values(self):
        self.env['iti.track'].create({
            'name': self.name,
            'description': self.description
        })

        # Search very important
        # students = self.env['iti.track'].search([('state', '=', 'accepted')])
        # # students.write({
        # #     'state': 'interviewing'
        # # })
        # # students.unlink()
        # print(students)
        # print(students.mapped('name'))
