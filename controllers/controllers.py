# -*- coding: utf-8 -*-
from odoo import http

# class Kyl(http.Controller):
#     @http.route('/kyl/kyl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kyl/kyl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kyl.listing', {
#             'root': '/kyl/kyl',
#             'objects': http.request.env['kyl.kyl'].search([]),
#         })

#     @http.route('/kyl/kyl/objects/<model("kyl.kyl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kyl.object', {
#             'object': obj
#         })