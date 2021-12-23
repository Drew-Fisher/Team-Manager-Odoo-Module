from odoo import fields,models


class Project(models.Model):
    _name = 'TeamManager.Project'
    _description = "Project Table"

    name = fields.Char(required=True)
    team_id = fields.Many2one('TeamManger.Team', ondelete='cascade',string="Team")