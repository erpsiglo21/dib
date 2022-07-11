# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import xlrd
import base64

from odoo import models, fields

class UploadProductState(models.TransientModel):
    _name = 'upload.product.state'
    _description = u'Carga el estado de un producto'

    file_diary = fields.Binary(string='Archivo', required=True)

    def parse_file(self):
        workbook = xlrd.open_workbook(file_contents=base64.b64decode(self.file_diary))
        sheet_names = workbook.sheet_names()

        for sheet_name in sheet_names:
            sheet = workbook.sheet_by_name(sheet_name)
            sheet_rows = sheet.nrows

            for row in range(1, sheet_rows):
                line = sheet._cell_values[row]
                product_id = self.env["product.template"].search([("default_code","=",line[0])])
                if product_id:
                    vals = {}
                    vals["sale_ok"] = True if line[1].upper() == "SI" else False
                    vals["purchase_ok"] = True if line[2].upper() == "SI" else False
                    product_id.write(vals)

