# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def write(self, values):
        res = super(SaleOrder, self).write(values)
        for picking in self.picking_ids:
            picking.scheduled_date = self.commitment_date

        return res