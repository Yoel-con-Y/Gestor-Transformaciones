from odoo import models, fields

class Transformaciones_Model(models.Model):
    _name = 'dragon_ball.transformaciones'
    _description = "Transformaciones de personajes"

    # Campos
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción', help='Introduce una descripción de la transformación')
    requisitos = fields.Text('Requisitos', help='Requisitos para alcanzar esta transformación')
    multiplicador = fields.Float('Multiplicador', default=1.0, help='Multiplicador al poder base del personaje')
    
    # Relación inversa: un personaje puede tener una transformación
    personaje_ids = fields.One2many('personaje.model', 'transformaciones_id', string="Personajes")

    
