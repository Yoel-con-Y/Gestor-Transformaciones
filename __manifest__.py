{
    'name': 'Gestor de Transformaciones',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'description': 'Este módulo permite gestionar transformaciones de Dragon Ball',
    'author': 'Yoel Francés & Elena Montserrat',
    'website': 'https://www.iespacomolla.es',
    'depends': ['base'],
    'data': [
       'views/view_personaje.xml',
       'views/view_transformaciones.xml',
       'security/ir.model.access.csv',
    ],
    'images': ['static/description/icon.png'],  # Asegura esta línea
    'installable': True,
    'application': True,
    'auto_install': False,
}