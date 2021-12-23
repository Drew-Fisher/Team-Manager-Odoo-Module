from odoo import fields, models


class Role(models.Model):
    _name = 'TeamManager.Role'
    _description = "Role table"

    name = fields.Char(required=True)
    employee_ids = fields.Many2many('TeamManager.Employee', string="Employees")