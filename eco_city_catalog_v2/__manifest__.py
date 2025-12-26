{
    'name': 'Eco City Catalog v2',
    'version': '17.0.1.0.0',
    'summary': 'Catálogo jerárquico de ubicación (país, departamento, ciudad, barrio)',
    'category': 'Contacts',
    'author': 'Juandelsur',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'security/eco_city_security.xml',
        'views/eco_city_views.xml',
        'views/eco_neighborhood_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
