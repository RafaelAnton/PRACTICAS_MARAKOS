# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stock_picking(models.Model):
    _inherit = 'stock.picking',

    stock_picking_barcode = fields.Char('Codigo de barras')

    @api.onchange('stock_picking_barcode')
    def onchange_barcode(self):
        for stock_picking in self:
            if stock_picking.stock_picking_barcode:
                result = stock_picking.pack_operation_product_ids.filtered(lambda p: p.product_id.barcode == stock_picking.stock_picking_barcode)
                if result.exists():
                    qty_done = result.qty_done + 1
                    result.qty_done = qty_done
                    stock_picking.stock_picking_barcode = ''

