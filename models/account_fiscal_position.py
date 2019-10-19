# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)

class AccountFiscalPosition(models.Model):


	_inherit = 'account.fiscal.position'

	list_name_id = fields.Many2one('account.fiscal.position.list.name', string = u'Régimen Fiscal')