# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def write(self, values):
        res = super(PurchaseOrder, self).write(values)
        for picking in self.picking_ids:
            picking.scheduled_date = self.date_planned
        return res