# -*- coding: utf-8 -*-
# from odoo import http


# class DuedateReminder(http.Controller):
#     @http.route('/duedate_reminder/duedate_reminder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/duedate_reminder/duedate_reminder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('duedate_reminder.listing', {
#             'root': '/duedate_reminder/duedate_reminder',
#             'objects': http.request.env['duedate_reminder.duedate_reminder'].search([]),
#         })

#     @http.route('/duedate_reminder/duedate_reminder/objects/<model("duedate_reminder.duedate_reminder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('duedate_reminder.object', {
#             'object': obj
#         })

