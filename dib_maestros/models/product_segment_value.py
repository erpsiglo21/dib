# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
#from odoo.exceptions import UserError


class ProductSegmentValue(models.Model):
    _name = "product.segment.value"
    _description = "Valores de segmentos de productos"

    #fields
    name = fields.Char(compute="_compute_name", readonly=True)
    value = fields.Char(string="Valor",required=True)
    segment_id = fields.Many2one(
        comodel_name="product.segment",
        required=True,
        string="Segment",
        )
    products_ids = fields.Many2many('product.template'
                                  ,'product_product_segment_value_rel'
                                  ,'segment_value_id'
                                  ,'product_tmpl_id'
                                  ,string='Products')
    segment_name = fields.Char(related="segment_id.name", string="Segment name")
    color = fields.Integer(related="segment_id.color", string="Color")
        
    @api.depends('segment_id.name','value')
    def _compute_name(self):
        for record in self:
            record.name = "{}: {}".format(record.segment_id.name, record.value)

    