# -*- coding: utf-8 -*-
from openerp import models, fields


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    campo_rescisao = fields.One2many(
        comodel_name='hr.field.rescission',
        inverse_name='rule',
        string='Campo da Rescisão',
    )
