# -*- coding: utf-8 -*-
# from odoo import http


# class ../../local/myLibrary(http.Controller):
#     @http.route('/../../local/my_library/../../local/my_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../local/my_library/../../local/my_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../local/my_library.listing', {
#             'root': '/../../local/my_library/../../local/my_library',
#             'objects': http.request.env['../../local/my_library.../../local/my_library'].search([]),
#         })

#     @http.route('/../../local/my_library/../../local/my_library/objects/<model("../../local/my_library.../../local/my_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../local/my_library.object', {
#             'object': obj
#         })
