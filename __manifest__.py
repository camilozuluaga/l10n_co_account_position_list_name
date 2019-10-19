# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name': 'l10n_co account position list name',
	'version': '1.0',
	'website': '',
	'category': 'Localizacion',
	'summary': 'l10n_co account position list name',
	'description': """
		modulo para el manejo de la informacion de las formas de pago de la factura

	""",
	'depends': [
		'account'
	],
	'data': [
		'data/account_fiscal_position_list_name_data.xml',
		'views/account_position_fiscal_list_name.xml',
		'views/account_fiscal_position.xml',
		'security/ir.model.access.csv',
		
	],
	'installable': True,
	'auto_install': False,
	'application': True,
}
