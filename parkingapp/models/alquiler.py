# -*- coding: utf-8 -*-
from re import S
from tracemalloc import DomainFilter
from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class alquiler(models.Model):
    _name = 'parkingapp.alquiler'
    #_auto = False
    _description = 'Alquiler'

    
    @api.depends('fecha_hora_ini','fecha_hora_fin')
    def _calcular_tiempo_alquiler (self):
            if (self.fecha_hora_ini and self.fecha_hora_fin):
                #self.tiempo_alquiler = (self.fecha_hora_fin - self.fecha_hora_ini).seconds
                self.tiempo_alquiler = (self.fecha_hora_fin - self.fecha_hora_ini).days
                        
        
    #name = fields.Integer(related='id', string='Código de Reserva', store=True)
    fecha_reserva = fields.Datetime(default=fields.Datetime.today)   
    fecha_hora_ini = fields.Datetime('Inicio', required=True)
    fecha_hora_fin = fields.Datetime('Fin', required=True)
    tiempo_alquiler = fields.Integer('Tiempo de Alquiler en Dias', compute='_calcular_tiempo_alquiler', store=True)
    
    
    estado_alquiler = fields.Selection([('pendiente', 'Pendiente'),('pagado', 'Pagado')],'Pago', default='pendiente')

    #relaciones entre tablas
    #conductor_id = fields.Many2one('parkingapp.conductor', string='Conductor')
    
    estacionamiento = fields.Many2one('parkingapp.estacionamiento',string='Estacionamiento')
    vehiculo_id = fields.Many2one('parkingapp.vehiculo', string='Patente' ,required=True)
          
    tipo_vehiculo = fields.Many2one(string='Tipo de vehículo', related='vehiculo_id.tipo_vehiculo_id')
    precio_alquiler_dia = fields.Float(string='Precio alquiler x día', related='tipo_vehiculo.precio_alquiler_dia')
    

    @api.depends('tiempo_alquiler','precio_alquiler_dia')
    def _calcular_monto_alquiler (self):
        for rec in self:
           if (rec.tiempo_alquiler and rec.precio_alquiler_dia):
                rec.monto = rec.tiempo_alquiler * rec.precio_alquiler_dia
               
            
    monto = fields.Float(string='Total a abonar', compute='_calcular_monto_alquiler', store=True) 
    parcela_id = fields.Many2one('parkingapp.parcela', string='Parcelas')
    #parcela_id = fields.Many2one('parkingapp.parcela', compute='calcular_parcela', string='Parcelas')
    
      
    def setear_pendiente(self):
        self.ensure_one()
        self.estado_alquiler = 'pendiente'
        #raise ValidationError('Se ha registrado el alquiler como pendiente de pago')
   
    def setear_pagado(self):
        self.ensure_one()
        self.estado_alquiler = 'pagado'
        #raise ValidationError('Se ha registrado el alquiler como pagado')

    #@api.depends('tipo_vehiculo') 
    #def calcular_parcela(self):
    # if tipo_vehiculo:
    #    ids=self.env['parkingapp.parcela'].search([['tipo_vehiculo_id', '=', 'Auto']])
        #ids=self.env['parkingapp.parcela'].search([['tipo_vehiculo_id', '=', self.tipo_vehiculo]])
        #ids=self.env['parkingapp.alquiler'].search([['fecha_hora_ini', '=', self.fecha_hora_ini]])
    #    auxIds=[]    
    #    for item in ids:
    #        auxIds.append(item.id) 
        #print ids
        #print auxIds
    #    return {'domain':{'organizerAccount':[('id','in',auxIds)]}} 

