from odoo import models, fields

# He hecho que este sea el modelo principal... creo
class Personaje_Model(models.Model):
    _name = "personaje.model"   # identificador del modelo
    _description = "Personajes de Dragon Ball Z"

    
    # Campos
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción', help='Introduce una descripción del personaje')
    raza = fields.Selection([
        ('saiyan', 'Saiyan'),
        ('human', 'Humano'),
        ('namekian', 'Namekiano'),
        ('frieza_race', 'Raza de Freezer'),
        ('android', 'Androide'),
        ('demon', 'Demonio'),
        ('other', 'Otro'),
    ], string="Raza", required=True)
    poder_base = fields.Integer(string="Poder Base", default=1000)
    control_ki = fields.Integer(string="Control de Ki", default=50)
    experiencia_batalla = fields.Integer(string="Experiencia de Batalla", default=0)
    imagen = fields.Binary("Imagen")
'''
    # Relación con modelo Transformaciones, habilitar cuando sepamos que funcionan ambos?
    transformation_ids = fields.One2many(
        'dragon_ball.transformation', 'character_id', string="Transformaciones"
    )'''