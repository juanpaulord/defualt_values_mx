# -*- coding: utf-8 -*-
from odoo import http

# class ../addons13/defaultMxValues(http.Controller):
#     @http.route('/../addons13/default_mx_values/../addons13/default_mx_values/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../addons13/default_mx_values/../addons13/default_mx_values/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../addons13/default_mx_values.listing', {
#             'root': '/../addons13/default_mx_values/../addons13/default_mx_values',
#             'objects': http.request.env['../addons13/default_mx_values.../addons13/default_mx_values'].search([]),
#         })

#     @http.route('/../addons13/default_mx_values/../addons13/default_mx_values/objects/<model("../addons13/default_mx_values.../addons13/default_mx_values"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../addons13/default_mx_values.object', {
#             'object': obj
#         })