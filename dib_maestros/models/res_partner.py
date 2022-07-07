# -*- coding: utf-8 -*-
import re
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = "res.partner"

    #Necesarios tanax
    canal_id = fields.Many2one('res.canal')
    codigo_interno = fields.Integer(string="Codigo interno")

