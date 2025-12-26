from odoo import models, fields

class EcoNeighborhood(models.Model):
    _name = 'eco.neighborhood'
    _description = 'Eco Neighborhood'

    name = fields.Char(required=True)
    city_id = fields.Many2one('eco.city', required=True)
    kind = fields.Selection([
        ('barrio', 'Barrio'),
        ('vereda', 'Vereda'),
    ], required=True)
