# -*- coding: utf-8 -*-
# from odoo import http


# class MtsCustom(http.Controller):
#     @http.route('/mts_custom/mts_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mts_custom/mts_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mts_custom.listing', {
#             'root': '/mts_custom/mts_custom',
#             'objects': http.request.env['mts_custom.mts_custom'].search([]),
#         })

#     @http.route('/mts_custom/mts_custom/objects/<model("mts_custom.mts_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mts_custom.object', {
#             'object': obj
#         })

