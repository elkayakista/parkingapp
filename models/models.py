# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api
from datetime import date, timedelta, time, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError




class estacionamiento(models.Model):
    _name = 'estacionamiento'
    _description = 'Estacionamiento'
    _order = 'name desc'

    name = fields.Char('Nombre de Estacionamiento', required=True)
    direccion = fields.Char('Dirección')
    telefono = fields.Integer('Teléfono')
    lavadero = fields.Boolean('Servicio de Lavado')
    inflado = fields.Boolean('Servicio de inflado de neumáticos')
    baño = fields.Boolean('Servicio de baño')
    hora_apertura = fields.Float('Hora de Apertura')
    hora_cierre = fields.Float('Hora de cierre')

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
    cubierta = fields.Boolean('Es Cubierta')

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
    fecha_nacimiento = fields.Date('Fecha Nacimiento')
    edad = fields.Integer('Edad')
    
   # relaciones entre tablas
    localidad_id = fields.Many2one('localidad', string='Localidad')
    vehiculo_ids = fields.Many2many('vehiculo', string='Vehículo')

   # restricciones por sql
    _sql_constraints=[('dni_uniq','unique(dni)','El dni ya existe')]

   
    
    #decorador para validad el formato de email
    @api.constrains('mail') 
    def validate_mail(self): 
        if self.mail: 
            match = re.match('^[_a-z]+[0-9-]*(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.mail) 
            if match == None: 
                 raise ValidationError('No es un E-mail válido')


    #decorador para blanquear campo edad cuando selecciono fecha_nacimiento
    @api.onchange('fecha_nacimiento')
    def _on_change_limpiar_edad(self):
        self.edad = ''
    

    #decorador para calcular edad
    @api.onchange('fecha_nacimiento')
    def set_age(self):
            for rec in self:
                if rec.fecha_nacimiento:
                        fmt = '%Y-%m-%d'
                        dt = rec.fecha_nacimiento
                        d1 = datetime.strptime(str(dt), fmt).date() 
                        d2 = date.today()    
                        rd = d2 - d1
                        rec.edad = rd.days / 365    


    # decorador para validad la edad
    @api.constrains('edad')
    def _check_Edad(self):
        for record in self:
            if record.edad < 18:
             raise ValidationError("Debe ser mayor a 18 años: %s" % record.edad)
                 
    
                 
##########################################################################################################

class pago(models.Model):
    _name = 'pago'
    _description = 'Pagos'

    name = fields.Char('Nombre de Pago', required=True)
    tipo_pago = fields.Selection([('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Mercadopago', 'Mercadopago')], 'tipo_pago', default="Mercadopago")


class reporte(models.Model):
    _name = 'reporte'
    _description = 'Reporte'

    name = fields.Char('Nombre de Reporte', required=True)
    #tipo_reporte = fields.Selection([('Ganancias_Mensual', 'Ganancias_Mensual'), ('Ocupacion_Parcelas', 'Ocupacion_parcelas'), ('Disponibilidad', 'Disponibilidad')], 'tipo_reporte', default="Ganancias_Mensual")
