from odoo import models, fields, api, _

class StockIn(models.Model):
    _name = 'inventory.stock.in'
    _description = 'Stock In Transaction'
    _rec_name = 'produk'

    no_trx = fields.Char(string='No. Transaksi', required=True, readonly=True, default=lambda self: _('New'))
    tanggal = fields.Date(string='Tanggal', required=True, default=fields.Date.today)
    produk = fields.Many2one('inventory.product', string='Product', required=True)
    sku = fields.Char(string='SKU', related='produk.sku', readonly=True)
    qty = fields.Integer(string='Jumlah', required=True)
    suplier = fields.Char(string='Supplier', required=True)
    keterangan = fields.Text(string='Keterangan')
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('no_trx', _('New')) == _('New'):
                vals['no_trx'] = self.env['ir.sequence'].next_by_code('inventory.stock.in') or _('New')
        result = super(StockIn, self).create(vals_list)
    
        for rec in result:
            if rec.produk:
                rec.produk.stock += rec.qty
        return result