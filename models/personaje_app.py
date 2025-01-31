from odoo import models, fields, api

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
    imagen = fields.Binary("Imagen", attachment=True)
    
    # Relación con Transformación: cada personaje tiene una única transformación
    transformaciones_id = fields.Many2one('dragon_ball.transformaciones', string="Transformación", ondelete='set null')

    # Campo calculado: Poder total del personaje, basado en el multiplicador de la transformación
    poder_total = fields.Integer('Poder Total', compute='_compute_poder_total', store=True)

    @api.depends('poder_base', 'transformaciones_id.multiplicador')
    def _compute_poder_total(self):
        for record in self:
            if record.transformaciones_id:
                record.poder_total = record.poder_base * record.transformaciones_id.multiplicador
            else:
                record.poder_total = record.poder_base

