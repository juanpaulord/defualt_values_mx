# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ValuesResPartner(models.Model):
    _inherit = 'res.partner'
    
    forma_de_pago = fields.Many2one('l10n_mx_edi.payment.method', string='Forma de pago')
    uso_id = fields.Selection([
        ('G01', 'Adquisición de mercancías'),
        ('G02', 'Devoluciones, descuentos o bonificaciones'),
        ('G03', 'Gastos en general'),
        ('I01', 'Construcciones'),
        ('I02', 'Mobilario y equipo de oficina por inversiones'),
        ('I03', 'Equipo de transporte'),
        ('I04', 'Equipo de cómputo y accesorios'),
        ('I05', 'Dados, troqueles, moldes, matrices y herramental'),
        ('I06', 'Comunicaciones telefónicas'),
        ('I07', 'Comunicaciones satelitales'),
        ('I08', 'Otra maquinaria y equipo'),
        ('D01', 'Honorarios médicos, dentales y gastos hospitalarios'),
        ('D02', 'Gastos médicos por incapacidad o discapacidad'),
        ('D03', 'Gastos funerales'),
        ('D04', 'Donativos'),
        ('D05', 'Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación)'),
        ('D06', 'Aportaciones voluntarias al SAR'),
        ('D07', 'Primas por seguros de gastos médicos'),
        ('D08', 'Gastos de transportación escolar obligatoria.'),
        ('D09', 'Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones.'),
        ('D10', 'Pagos por servicios educativos (colegiaturas)'),
        ('P01', 'Por definir'),
    ], 'Uso', default='P01',
        help='Used in CFDI 3.3 to express the key to the usage that will '
        'gives the receiver to this invoice. This value is defined by the '
        'customer. \nNote: It is not cause for cancellation if the key set is '
        'not the usage that will give the receiver of the document.')


class ValuesAccountPartner(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id')
    def _value_def(self):
        if self.partner_id.forma_de_pago:
            self.l10n_mx_edi_payment_method_id = self.partner_id.forma_de_pago.id
        else:
            self.l10n_mx_edi_payment_method_id=''

        if self.partner_id.uso_id:
            self.l10n_mx_edi_usage = self.partner_id.uso_id
        else:
            self.l10n_mx_edi_usage=''
    


class DefaultValuesInvoice(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        journal = self.env['account.move'].with_context(force_company=self.company_id.id, default_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

        invoice_vals = {
            'ref': self.client_order_ref or '',
            'type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'invoice_payment_ref': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'l10n_mx_edi_payment_method_id': self.partner_id.forma_de_pago.id,
            'l10n_mx_edi_usage': self.partner_id.uso_id,
        }
        return invoice_vals

#    @api.depends('partner_id')
#    def _value_def(self):
#        if self.partner_id.forma_de_pago:
#            self.l10n_mx_edi_payment_method_id = self.partner_id.forma_de_pago.id
#        else:
#            self.l10n_mx_edi_payment_method_id=''
#
#       if self.partner_id.uso_id:
#            self.l10n_mx_edi_usage = self.partner_id.uso_id
#        else:
#            self.l10n_mx_edi_usage=''
# class ../addons13/default_mx_values(models.Model):
#     _name = '../addons13/default_mx_values.../addons13/default_mx_values'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
