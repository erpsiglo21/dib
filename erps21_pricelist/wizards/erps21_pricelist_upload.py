# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import xlrd
import base64

from odoo import models, fields
from odoo.exceptions import UserError
from odoo.tools.translate import _

class Erps21PricelistUpload(models.TransientModel):
    _name = 'erps21.pricelist.upload'
    _description = u'Carga de lista de precios'

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id    

    name = fields.Char(string="Lista de precio", required=True)
    currency_id = fields.Many2one('res.currency', 'Moneda', default=_get_default_currency_id, required=True)
    file_diary = fields.Binary(string='Archivo', required=True)

    def parse_file(self):        
        workbook = xlrd.open_workbook(file_contents=base64.b64decode(self.file_diary))
        sheet_names = workbook.sheet_names()

        productPricelistORM = self.env["product.pricelist"]
        productProductORM = self.env["product.product"]

        #Verifica si la lista existe
        priceList = productPricelistORM.search([("name","=",self.name)])
        item_ids = [(5,0,0)] if priceList else []

        for sheet_name in sheet_names:
            sheet = workbook.sheet_by_name(sheet_name)
            sheet_rows = sheet.nrows
            primera = True

            for row in range(sheet_rows):
                line = sheet._cell_values[row]

                if primera:
                    primera = False
                    continue

                #Busca el producto
                product_id = None
                try:
                    product_id = productProductORM.search([('default_code', '=', "{:.0f}".format(line[0]))],limit=1)
                except:
                    product_id = productProductORM.search([('default_code', '=', "{}".format(line[0]))],limit=1)

                if not product_id:
                    raise UserError(_('El producto "{:.0f}" debe estar definido'.format(line[0])))

                item_ids.append((0,0,{
                    "product_tmpl_id": product_id.product_tmpl_id.id,
                    "applied_on": "1_product",
                    "base": "list_price",
                    "company_id": self.env.company.id,
                    "currency_id": self.currency_id.id,
                    "fixed_price": line[1]
                }))

        if not priceList:
            priceList = productPricelistORM.create({
                            "name": self.name.strip(),
                            "company_id": self.env.company.id,
                            "currency_id": self.currency_id.id,
                            "item_ids": item_ids
                        })
        else:
            priceList.write({"item_ids": item_ids})
