# MTS - MODELO DE TICKET DE HELPDESK

from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    x_name = fields.Char(string='Nombre del ticket', required=True)
    x_partner_id = fields.Many2one('res.partner', string='Cliente')
    x_state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_progreso', 'En Progreso'),
        ('resuelto', 'Resuelto'),
    ], string='Estado', default='nuevo')
    x_description = fields.Text(string='Descripción del problema')
    x_create_date = fields.Datetime(string='Fecha de creación', default=fields.Datetime.now)
    x_user_id = fields.Many2one('res.users', string='Usuario asignado')

    def action_mark_as_resolved(self):
        self.write({'state': 'resuelto'})
