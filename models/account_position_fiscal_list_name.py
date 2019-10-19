# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)

class AccountPositionListName(models.Model):


	_name = 'account.position.fiscal.list.name'


	name = fields.Char(string=u'Name')
	code = fields.Char(string=u'Code')
	list_name_id = fields.Many2one('account.position.fiscal', string = 'Position Fiscal')
