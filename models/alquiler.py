# -*- coding: utf-8 -*-
from re import S
from tracemalloc import DomainFilter
from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class alquiler(models.Model):
    _name = 'alquiler'
    _description = 'Alquiler'
    _order = 'fecha_hora_ini desc'                  
        
    fecha_reserva = fields.Datetime(default=fields.Datetime.today)   
    fecha_hora_ini = fields.Datetime('Inicio', required=True)
    fecha_hora_fin = fields.Datetime('Fin', required=True)
    tiempo_alquiler = fields.Integer('Tiempo de Alquiler en Dias', compute='_calcular_tiempo_alquiler', store=True)   
    estado_alquiler = fields.Selection([('pendiente', 'Pendiente'),('pagado', 'Pagado')],'Pago', default='pendiente')
    precio_alquiler_dia = fields.Float(string='Precio alquiler x día', 
    related='tipo_vehiculo.precio_alquiler_dia')
    

    #relaciones entre tablas
     
    estacionamiento = fields.Many2one('estacionamiento',string='Estacionamiento')
    vehiculo_id = fields.Many2one('vehiculo', string='Patente' ,required=True)  
    conductor_id = fields.Many2one('conductor', string='Conductor',required=True)

    tipo_vehiculo = fields.Many2one(string='Tipo de vehículo', related='vehiculo_id.tipo_vehiculo_id')


    @api.depends('fecha_hora_ini','fecha_hora_fin')
    def _calcular_tiempo_alquiler (self):
        if (self.fecha_hora_ini and self.fecha_hora_fin):
           self.tiempo_alquiler = (self.fecha_hora_fin - self.fecha_hora_ini).days
 

    
    @api.depends('tiempo_alquiler','precio_alquiler_dia')
    def _calcular_monto_alquiler (self):
        for rec in self:
           if (rec.tiempo_alquiler and rec.precio_alquiler_dia):
                rec.monto = rec.tiempo_alquiler * rec.precio_alquiler_dia
    
    
    monto = fields.Float(string='Total a abonar', compute='_calcular_monto_alquiler', store=True) 
    
    parcela_cubierta = fields.Boolean(string='Parcela Cubierta')
    
    parcela_id = fields.Many2one('parcela', string='Parcelas')
             
          
    def setear_pendiente(self):
        self.ensure_one()
        self.estado_alquiler = 'pendiente'
        
   
    def setear_pagado(self):
        self.ensure_one()
        self.estado_alquiler = 'pagado'

    
    #Decorador para blanquear campo conductor y parcela cuando selecciono vehículo
    @api.onchange('vehiculo_id')
    def _on_change_limpiar(self):
        self.conductor_id = ''
        self.parcela_id = ''  
       
    #Decorador para validar parcela disponible
    #@api.onchange('tipo_vehiculo')
    #def _on_change_validar_parcela(self):
    #    if self.parcela_id:   
            


    #    self.fecha_hora_fin
    #    self.fecha_hora_ini
    #    self.parcela_id = ''


    #@api.multi
    #@api.depends('fact_ids')
    #def _obtener_datos(self):


