# Copyright 2020 haulogy SA/NV (<https://www.haulogy.net/>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestIrUiView(common.TransactionCase):
    def test_action_preview(self):
        view = self.env.ref("base.view_view_form")
        action = view.action_preview()
        self.assertEquals(
            action.get("context"),
            {
                "edit": False,
                "create": False,
                "delete": False,
                "duplicate": False,
                "form_view_initial_mode": "readonly",
            },
        )
        self.assertEquals(action.get("target"), "current")
