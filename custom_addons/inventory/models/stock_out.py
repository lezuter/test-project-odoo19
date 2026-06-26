from odoo import models, fields, api, _

class StockOut(models.Model):
    _name = 'inventory.stock.out'
    _description = 'Stock Out Transaction'
    _rec_name = 'produk'

    no_trx = fields.Char(string='No. Transaksi', required=True, readonly=True, default=lambda self: _('New'))
    tanggal = fields.Date(string='Tanggal', required=True, default=fields.Date.today)
    produk = fields.Many2one('inventory.product', string='Product', required=True, domain=[('stock', '>', 0) ])
    sku = fields.Char(string='SKU', related='produk.sku', readonly=True)
    qty = fields.Integer(string='Jumlah', required=True)
    penerima = fields.Char(string='Penerima', required=True)
    tipe = fields.Selection([
        ('pasien', 'Pemberian Pasien (Resep/Rawat)'),
        ('mutasi', 'Mutasi / Pindah Gudang'),
        ('retur_vendor', 'Retur ke Vendor / Supplier'),
        ('kadaluarsa', 'Barang Kadaluarsa (Expired)'),
    ], string='Tipe', default='pasien', required=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('no_trx', _('New')) == _('New'):
                vals['no_trx'] = self.env['ir.sequence'].next_by_code('inventory.stock.out') or _('New')
        
        result = super(StockOut, self).create(vals_list)
    
        for rec in result:
            if rec.produk:
             rec.produk.stock -= rec.qty

        return result