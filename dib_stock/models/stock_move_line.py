# -*- coding: utf-8 -*-

from odoo import api, models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'
    rotulate = fields.Char(compute='_check_move_line_description',string="Rotulado")

    def _check_move_line_description(self):
        '''
        If product description is different from de Sale Order name,then rotulate is seted. Else None.
        '''
        for record in self:
            #if record.sale_line_id and record.sale_line_id.name == record.product_id.product_tmpl_id.name:
            if record.sale_line_id:
                record.rotulate = 'rerotular' if record.sale_line_id.name != record.product_id.product_tmpl_id.display_name else None
            else:
                record.rotulate = None

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    rotulate = fields.Char(compute='_get_rotulate',string="Rotulado")

    def _get_rotulate(self):
        '''
        Get Rotulate field from Stock move, by move id
        '''
        for record in self:
            record.rotulate = record.move_id.rotulate if record.move_id.rotulate else None


