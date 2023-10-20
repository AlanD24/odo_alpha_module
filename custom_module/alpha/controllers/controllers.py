# -*- coding: utf-8 -*-
# from odoo import http


# class Alpha(http.Controller):
#     @http.route('/alpha/alpha', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alpha/alpha/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alpha.listing', {
#             'root': '/alpha/alpha',
#             'objects': http.request.env['alpha.alpha'].search([]),
#         })

#     @http.route('/alpha/alpha/objects/<model("alpha.alpha"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alpha.object', {
#             'object': obj
#         })
