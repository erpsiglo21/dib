# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
#from odoo.exceptions import UserError


class ProductSegmentValue(models.Model):
    _name = "product.segment.value"
    _description = "Modelo para creacion de valores para segmentos DIB"

    #fields
    value = fields.Char(string="Valor",required=True)
    segment_id = fields.Many2one(
        comodel_name="product.segment",
        required=True,
        string="Segment",
        )
        
    def name_get(self):
        ret = []
        for record in self:
            ret.append("{}:{}".format(record.segment_id.name,record.value))
        return ret

    