# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools


class StockValuationLayer(models.Model):
    """Stock Valuation Layer"""

    _inherit = 'stock.valuation.layer'

    location = fields.Char(compute='_get_location',string="Ubicacion")

    def _get_location(self):
        for record in self:
            record.location = record.stock_move_id.location_dest_id.display_name


