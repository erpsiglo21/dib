# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
#from odoo.exceptions import UserError


class ProductSegment(models.Model):
    _name = "product.segment"
    _description = "Modelo para creacion de segmentos DIB"

    #fields
    name = fields.Char(string="Description",required=True)
    type = fields.Selection([("one", "unique value for product"), ("multi", "multiple value for product")],string="Type",required=True,default="one",)
    value_ids = fields.One2many(
        comodel_name="product.segment.value", inverse_name="segment_id", string="Values"
    )