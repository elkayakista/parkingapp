# -*- coding: utf-8 -*-
from xmlrpc.client import DateTime
from odoo import models, fields, api



class alquiler(models.Model):
    _name = 'parkingapp.alquiler'
    #_auto = False
    _description = 'Alquileres por día'

    #@api.one
    @api.depends('fecha_hora_ini','fecha_hora_fin')
    def _calcular_tiempo_alquiler (self):
        if (self.fecha_hora_ini):
        #   ini = fields.Datetime.to_string(self.fecha_hora_ini)
        #    fin = fields.Datetime.to_string(self.fecha_hora_fin)
        #    self.tiempo_alquiler = self.fecha_hora_fin - timedelta(self.fecha_hora_ini)
        #    self.tiempo_alquiler = fields.Date.from_string(fin) - fields.Date.from_string(ini)
            self.tiempo_alquiler = 1

    name = fields.Char('Código')
    fecha_reserva = fields.Datetime(default=fields.Datetime.today)
        
    fecha_hora_ini = fields.Datetime('Inicio', required=True)
    fecha_hora_fin = fields.Datetime('Fin', required=True)
    #tiempo_alquiler = fields.Integer('Tiempo de Alquiler en Horas', required=True)
    tiempo_alquiler = fields.Integer('Tiempo de Alquiler en Horas', compute='_calcular_tiempo_alquiler', store=True)
    estado_alquiler = fields.Selection([('pagado', 'Pagado'),('pendiente', 'Pendiente')],'Estado', default='pendiente')

    #relaciones entre tablas
    #conductor_id = fields.Many2one('parkingapp.conductor', string='Conductor')
    parcela_id = fields.Many2one('parkingapp.parcela', string='Parcela')
    vehiculo_id = fields.Many2one('parkingapp.vehiculo', string='Patente')

    # restricciones por sql
    _sql_constraints=[('name_uniq','unique(name)','El codigo de identificaciòn de alquiler ya existe - Por favor escoja otro')]

    