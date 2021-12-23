from odoo import fields,models


class Employee(models.Model):
    _name = 'TeamManager.Employee'
    _description = "Employee Table"

    name = fields.Char(required=True)
    role_id = fields.Many2many('TeamManager.Role', string="Roles")
    team_id = fields.Many2one('TeamManager.Team', ondelete='cascade', string="Team")