# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    segment_ids = fields.Many2many('product.segment.value'
                                  ,'product_product_segment_value_rel'
                                  ,'product_tmpl_id'
                                  ,'segment_value_id'
                                  ,string='Segments')

    @api.constrains('segment_ids')
    def _check_segments(self):
        for record in self:
            for segment in record.segment_ids:
                if segment.segment_id.type == "one":
                    same_segment = record.segment_ids.filtered(lambda x: x.segment_id == segment.segment_id)
                    if len(same_segment) > 1:
                        raise ValidationError(_("You cannot set multiple values for segment '{}'".format(segment.segment_name)))
