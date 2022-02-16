# -*- coding: utf-8 -*-
from odoo import models, fields, api


class estacionamiento(models.Model):
    _name = 'parkingapp.estacionamiento'
    _description = 'Estacionamiento'

    name = fields.Char('Nombre de Estacionamiento', required=True)
    direccion = fields.Char('Dirección')
    telefono = fields.Integer('Teléfono')

 # relaciones entre tablas
    localidad_id = fields.Many2one('parkingapp.localidad', string='Localidad')
    parcela_ids = fields.One2many('parkingapp.parcela','estacionamiento_id',string='Parcelas')

 # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','El nombre del estacionamiento ya existe')]
    


class parcela(models.Model):
    _name = 'parkingapp.parcela'
    _description = 'Parcela de Estacionaiento'

    name = fields.Char('Código de Parcela', required=True)
    descripcion = fields.Char('Descripción')

 # relaciones entre tablas
    tipo_vehiculo_id = fields.Many2one('parkingapp.tipo_vehiculo', string='Tipo de vehìculo admitido')
    estacionamiento_id = fields.Many2one('parkingapp.estacionamiento',string='Estacionamiento')
   
    #alquiler_ids = fields.One2many('parkingapp.alquiler','',string='Alquiler')
   

# restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','El codigo de identificaciòn de la parcela ya existe - Por favor escoja otro')]



class localidad(models.Model):
    _name = 'parkingapp.localidad'
    _description = 'Localidad'

    name = fields.Char('Localildad', required=True)
    
 # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','La Localidad ya existe')]



class tipo_vehiculo(models.Model):
    _name = 'parkingapp.tipo_vehiculo'
    _description = 'Tipos de vehìculos admitidos'

    name = fields.Char('Tipo vehículo',required=True)
    #tipo_vehiculo = fields.Selection([('Auto', 'Automovil'), ('Suv', 'Camioneta'), ('Moto', 'Motocicleta')], 'tipo_admitido', default="Auto")
    
    #precio_reserva_hora = fields.Float(string='Precio reserva x hora')
    precio_alquiler_dia = fields.Float(string='Precio alquiler x día',required=True)

 # restricciones por sql
    sql_constraints=[('name_uniq','unique(name)','El tipo de vehículo ya existe')]

    

class vehiculo(models.Model):
    _name = 'parkingapp.vehiculo'
    _description = 'Vehiculos de Estacionamiento'

    name = fields.Char('Patente', required=True)
    marca = fields.Char('Marca')
    modelo = fields.Char('Modelo')
    

  # relaciones entre tablas
    #conductor_ids = fields.Many2many('res.partner',string='Conductor de Vehìculo')
    conductor_ids = fields.Many2many('parkingapp.conductor',string='Conductor de Vehìculo')
    tipo_vehiculo_id = fields.Many2one('parkingapp.tipo_vehiculo', string='Tipo de vehìculo')   

 # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','La patente ya existe')]



class conductor(models.Model):
    #_inherit = 'res.partner'
    _name = 'parkingapp.conductor'
    _description = 'Conductores'

    name = fields.Char('Apellido', required=True)
    nombre = fields.Char('Nombre', required=True)
    dni = fields.Integer('D.N.I', required=True)
    direccion = fields.Char('Direción')
    telefono = fields.Integer('Telefono')
    mail = fields.Char('Mail')


 # relaciones entre tablas
    localidad_id = fields.Many2one('parkingapp.localidad', string='Localidad')
    vehiculo_ids = fields.Many2many('parkingapp.vehiculo', string='Vehículo')

 # restricciones por sql
    _sql_constraints=[('dni_uniq','unique(dni)','El dni ya existe')]

##########################################################################################################

class pago(models.Model):
    _name = 'parkingapp.pago'
    _description = 'Pagos'

    name = fields.Char('Nombre de Pago', required=True)
    tipo_pago = fields.Selection([('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Mercadopago', 'Mercadopago')], 'tipo_pago', default="Mercadopago")


class reporte(models.Model):
    _name = 'parkingapp.reporte'
    _description = 'Reportes'

    name = fields.Char('Nombre de Reporte', required=True)
    tipo_reporte = fields.Selection([('Ganancias_Mensual', 'Ganancias_Mensual'), ('Ocupacion_Parcelas', 'Ocupacion_parcelas'), ('Disponibilidad', 'Disponibilidad')], 'tipo_reporte', default="Ganancias_Mensual")

