# Copyright 2020 haulogy SA/NV (<https://www.haulogy.net/>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def action_preview(self):
        return {
            "name": "Preview view",
            "type": "ir.actions.act_window",
            "res_model": self.model,
            "view_mode": self.type,
            "target": "current",
            "view_id": self.id,
            "context": {
                "edit": False,
                "create": False,
                "delete": False,
                "duplicate": False,
                "form_view_initial_mode": "readonly",
            },
        }
