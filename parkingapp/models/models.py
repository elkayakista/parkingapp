# -*- coding: utf-8 -*-
from odoo import models, fields, api


class estacionamiento(models.Model):
    _name = 'estacionamiento'
    _description = 'Estacionamiento'

    name = fields.Char('Nombre de Estacionamiento', required=True)
    direccion = fields.Char('Dirección')
    telefono = fields.Integer('Teléfono')

 # relaciones entre tablas
    localidad_id = fields.Many2one('localidad', string='Localidad')
    parcela_ids = fields.One2many('parcela','estacionamiento_id',string='Parcelas')

 # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','El nombre del estacionamiento ya existe')]
    


class parcela(models.Model):
    _name = 'parcela'
    _description = 'Parcela de Estacionaiento'

    name = fields.Char('Código de Parcela', required=True)
    descripcion = fields.Char('Descripción')

 # relaciones entre tablas
    tipo_vehiculo_id = fields.Many2one('tipo_vehiculo', string='Tipo de vehìculo admitido')
    estacionamiento_id = fields.Many2one('estacionamiento',string='Estacionamiento')
   
    alquiler_ids = fields.One2many('alquiler','parcela_id',string='Alquiler')
   

# restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','El codigo de identificaciòn de la parcela ya existe - Por favor escoja otro')]



class localidad(models.Model):
    _name = 'localidad'
    _description = 'Localidad'

    name = fields.Char('Localildad', required=True)
    
 # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','La Localidad ya existe')]



class tipo_vehiculo(models.Model):
    _name = 'tipo_vehiculo'
    _description = 'Tipos de vehìculos admitidos'

    name = fields.Char('Tipo vehículo',required=True)
   
    precio_alquiler_dia = fields.Float(string='Precio alquiler x día',required=True)

 # restricciones por sql
    sql_constraints=[('name_uniq','unique(name)','El tipo de vehículo ya existe')]

    

class vehiculo(models.Model):
    _name = 'vehiculo'
    _description = 'Vehiculos de Estacionamiento'

    name = fields.Char('Patente', required=True)
    marca = fields.Char('Marca')
    modelo = fields.Char('Modelo')
    

  # relaciones entre tablas
    conductor_ids = fields.Many2many('conductor',string='Conductor de Vehìculo')
    tipo_vehiculo_id = fields.Many2one('tipo_vehiculo', string='Tipo de vehìculo')   

 # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','La patente ya existe')]



class conductor(models.Model):
    _name = 'conductor'
    #_inherit = 'res.partner'
    
    _description = 'Conductores'

    name = fields.Char('Apellido', required=True)
    nombre = fields.Char('Nombre', required=True)
    dni = fields.Integer('D.N.I', required=True)
    direccion = fields.Char('Direción')
    telefono = fields.Integer('Telefono')
    mail = fields.Char('Mail')


 # relaciones entre tablas
    localidad_id = fields.Many2one('localidad', string='Localidad')
    vehiculo_ids = fields.Many2many('vehiculo', string='Vehículo')

 # restricciones por sql
    _sql_constraints=[('dni_uniq','unique(dni)','El dni ya existe')]

##########################################################################################################

class pago(models.Model):
    _name = 'pago'
    _description = 'Pagos'

    name = fields.Char('Nombre de Pago', required=True)
    tipo_pago = fields.Selection([('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Mercadopago', 'Mercadopago')], 'tipo_pago', default="Mercadopago")

