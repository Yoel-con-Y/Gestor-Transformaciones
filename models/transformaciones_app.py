from odoo import models, fields

class Transformaciones_Model(models.Model):
    _name = "transformaciones.model"
    _description = "App que permite gestionar la compra/venta de viviendas"

    # Campos básicos
    name = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción', help='Introduce una descripción de la propiedad')
    cpostal = fields.Char('Código Postal', required=True)
    fecha_disponible = fields.Date('Fecha disponible')
    precio_inicial = fields.Float('Precio inicial', required=True)
    precio_venta = fields.Float('Precio venta', required=True)
    habitaciones = fields.Integer('Nº habitaciones', required=True)
    m_utiles = fields.Integer('Metros útiles', required=True)
    garage = fields.Boolean('Garage')
    jardin = fields.Boolean('Jardín')
    m_jardin = fields.Integer('Metros jardín')
    orientacion = fields.Selection(
        string='Orientación',
        selection=[('norte', 'Norte'), ('sur', 'Sur'), ('este', 'Este'), ('oeste', 'Oeste')])

    # Campos adicionales para los widgets
    color = fields.Char('Color')  # Campo para el widget 'color'
    status = fields.Selection(
        [('draft', 'Borrador'), ('sold', 'Vendido')],
        default='draft', string='Estado')  # Campo para el widget 'statusbar'
    imagen_vivienda = fields.Binary("Imagen de Vivienda", attachment=True)
