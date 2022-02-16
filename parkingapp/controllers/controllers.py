# -*- coding: utf-8 -*-

from odoo import http

class SiedCloud(http.Controller):
    @http.route('/parkingapp_module/', auth='public')
    def index(self, **kw):
        return "Y(°_°)Y"

# class Parkingapp(http.Controller):
#     @http.route('/parkingapp/parkingapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parkingapp/parkingapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parkingapp.listing', {
#             'root': '/parkingapp/parkingapp',
#             'objects': http.request.env['parkingapp.parkingapp'].search([]),
#         })

#     @http.route('/parkingapp/parkingapp/objects/<model("parkingapp.parkingapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parkingapp.object', {
#             'object': obj
#         })
