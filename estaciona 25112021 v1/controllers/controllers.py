# -*- coding: utf-8 -*-
from odoo import http


class Estaciona(http.Controller):
    @http.route('/estaciona', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/estaciona/estaciona/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estaciona.listing', {
#             'root': '/estaciona/estaciona',
#             'objects': http.request.env['estaciona.estaciona'].search([]),
#         })

#     @http.route('/estaciona/estaciona/objects/<model("estaciona.estaciona"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estaciona.object', {
#             'object': obj
#         })
