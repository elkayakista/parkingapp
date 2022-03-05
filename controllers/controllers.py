# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class ParkingApp(http.Controller):
    @http.route('/parkingapp/', auth='public')
    def index(self, **kw):
        return "Si ves esto esta funcionando bien el decorador http.route"





class Parkingapp(http.Controller):
    
    @http.route('/parkingapp/alquileres/objects/<model("alquiler"):alquiler>/', auth='public')
    def alquiler(self, alquiler, **kw):
        return http.request.render('alquiler', {
             'alquiler': alquiler
         })
