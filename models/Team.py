from odoo import fields, models


class Team(models.Model):
    _name = 'team.model'
    _description = "Team Table"

    name = fields.Char(string="Name", required=True)
    size = fields.Integer(string="Team Size")
    employee_ids = fields.One2many('TeamManager.Employee', 'team_id', string="Members")
    project_ids = fields.One2many('TeamManager.Projects', 'project_ids', string="Projects")