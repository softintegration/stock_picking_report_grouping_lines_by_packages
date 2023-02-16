# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _get_qty_ordered_from_aggregated_product(self,strict=False):
        aggregated_move_lines = self._get_aggregated_product_quantities(strict=strict)
        qty_ordered = {}
        for each in self:
            description = each.move_id.description_picking
            if description == each.product_id.display_name or description == each.product_id.name:
                description = False
            qty_ordered_line_key = f'{each.product_id.id}_{each.product_id.display_name}_{description or ""}_{each.product_uom_id.id}'
            qty_ordered[each.id] = aggregated_move_lines[qty_ordered_line_key]
        return qty_ordered


