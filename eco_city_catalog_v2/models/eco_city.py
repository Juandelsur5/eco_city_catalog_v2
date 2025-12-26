from odoo import models, fields

class EcoCity(models.Model):
    _name = 'eco.city'
    _description = 'Eco City'

    name = fields.Char(required=True)
    state_id = fields.Many2one('res.country.state', required=True)
    country_id = fields.Many2one(related='state_id.country_id', store=True)
