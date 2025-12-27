from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    eco_country_id = fields.Many2one(
        'res.country',
        string='Country'
    )

    eco_state_id = fields.Many2one(
        'res.country.state',
        string='State',
        domain="[('country_id', '=', eco_country_id)]"
    )

    eco_city_id = fields.Many2one(
        'eco.city',
        string='City',
        domain="[('state_id', '=', eco_state_id)]"
    )

    eco_neighborhood_id = fields.Many2one(
        'eco.neighborhood',
        string='Neighborhood',
        domain="[('city_id', '=', eco_city_id)]"
    )

    @api.onchange('eco_country_id')
    def _onchange_eco_country(self):
        self.eco_state_id = False
        self.eco_city_id = False
        self.eco_neighborhood_id = False

    @api.onchange('eco_state_id')
    def _onchange_eco_state(self):
        self.eco_city_id = False
        self.eco_neighborhood_id = False

    @api.onchange('eco_city_id')
    def _onchange_eco_city(self):
        self.eco_neighborhood_id = False
        if self.eco_city_id:
            self.city = self.eco_city_id.name
