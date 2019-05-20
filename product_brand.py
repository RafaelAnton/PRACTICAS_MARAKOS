# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product_Brand(models.Model):
    _name = "procut_brand"
    _rec_name = 'brand_name'

    brand_name = fields.Char('Marca De Producto')