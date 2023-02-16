# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    grouping_move_lines_by_packages = fields.Boolean(
        string='Grouping move lines by packages in report', default=False,
        help="If this case is checked,the system will group the move lines of the picking by packages in the report.")

