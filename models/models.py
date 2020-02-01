# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NotaVenta(models.Model):
    _inherit = 'sale.order'

    driver_id = fields.Many2one('res.partner', 'Conductor', track_visibility="onchange", help='Conductor del Vehiculo', copy=False)

class NewModule(models.Model):
    _inherit = 'purchase.order'

    flota_id = fields.Many2one(comodel_name="fleet.vehicle", string="Caminion", required=False, )

class FacturaCompra(models.Model):
    _inherit = 'account.invoice'

    flota_id = fields.Many2one(comodel_name="fleet.vehicle", string="Caminion", required=False, )
    tipo_servicio_id = fields.Many2one(comodel_name="fleet.service.type", string="Tipo de Servicio", required=False, )

    @api.multi
    def action_invoice_open(self):
        fleet_vehicle = self.env['fleet.vehicle']
        factura= super(FacturaCompra, self).action_invoice_open()
        #self.env.cr.execute("SELECT id, num_bl FROM stock_picking WHERE state='done' and invoice_state='2binvoiced' and partner_id= %d" %(partner) )
        if self.flota_id:
            new_rec = self.env['fleet.vehicle.cost'].create({
                'name': self.partner_id.name,  # many2one must be an integer value
                'vehicle_id': self.flota_id.id,
                'cost_subtype_id': self.tipo_servicio_id.id,
                'amount': self.amount_untaxed,
                'cost_type':'services',
                'date': self.date_invoice,
                'description':self.tipo_servicio_id.name,
                'create_uid':1,
                'create_date': self.date_invoice,
                'write_uid':1,
                'write_date':self.date_invoice
            })
