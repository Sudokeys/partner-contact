# -*- coding: utf-8 -*-

{
    "name": 'partner_prospect',
    "description": u"""
Partner prospect:
=================

This module will add prospect boolean field on res.partner.

- With this you can manage a partner before becoming customer or supplier
- New Prospect menu is available under Sales -> sales
- New search view and action is also available

Thanks to:
==========

If you have a question you can contact one of the following contributors:

- Nicolas JEUDY <nicolas@sudokeys.com>
""",
    "version": "1.1",
    "depends": [
        'base', 'crm', 'sales_team',
    ],
    "author": "Sudokeys",
    "category": "CRM",
    "installable" : True,
    "auto_install" : False,
    "data": [
        'res_partner_view.xml',
        'ir_ui_view_record.xml',
        'ir_actions_act_window_record.xml',
        'ir_ui_menu_record.xml',
        'ir_actions_act_window_view_record.xml',
        'crm_lead_view.xml',
    ],
}
