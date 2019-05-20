# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product_Brand(models.Model):

    _inherit = 'product.template'

    marca_producto = fields.Many2one('procut_brand',u'Marca de Productos')