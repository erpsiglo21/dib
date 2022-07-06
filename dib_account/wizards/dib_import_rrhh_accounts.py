# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import xlrd
import base64

from odoo import models, fields
from odoo.exceptions import UserError
from odoo.tools.translate import _

class RRHHAccountEntriesUpload(models.TransientModel):
    _name = 'rrhh.account.entries.upload'
    _description = u'Carga de asientos contables de RRHH'

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id    

    currency_id = fields.Many2one('res.currency', 'Moneda', default=_get_default_currency_id, required=True)
    file_diary = fields.Binary(string='Archivo', required=True)

    def parse_file(self):
        current_move_id = self.env.context.get("current_move")
        current_move = self.env["account.move"].browse(current_move_id)
        workbook = xlrd.open_workbook(file_contents=base64.b64decode(self.file_diary))
        sheet_names = workbook.sheet_names()
        company_id = self.env.company.id
        entry_lines_to_add = []

        for sheet_name in sheet_names:
            sheet = workbook.sheet_by_name(sheet_name)
            sheet_rows = sheet.nrows

            for row in range(sheet_rows):
                line = sheet._cell_values[row]
                current_account_number = line[0].replace("-","")
                current_account = self.env["account.account"].search([("code","=",current_account_number)])  
                entry_lines_to_add.append((0,0,{
                     "account_id": current_account.id,
                     "partner_id": company_id,
                     "name": line[1],
                     "debit": line[4],
                     "credit": line[5]
                }))
        current_move.write({'line_ids':entry_lines_to_add})            

