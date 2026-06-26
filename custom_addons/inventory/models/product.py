from odoo import models, fields

class InventoryProduct(models.Model):
    _name = 'inventory.product'
    _description = 'Master Data Product'
    _rec_name = 'produk'

    produk = fields.Char(string='Product Name', required=True)
    sku = fields.Char(string='SKU', required=True)
    kategori = fields.Selection([
        ('alkes', 'Alkes'),
        ('consumable', 'Consumable'),
        ('obat', 'Obat'),
        ('lainnya', 'Lainnya')
    ], string='Kategori', default='lainnya', required=True)
    stock = fields.Integer(string='Stock', default=0, readonly=True)
    satuan = fields.Selection([
        ('pcs', 'Pcs'),
        ('botol', 'Botol'),
        ('tablet', 'Tablet'),
        ('kapsul', 'Kapsul'),
        ('box', 'Box'),
        ('strip', 'Strip')
    ], string='Satuan', default='pcs', required=True)
    rak = fields.Selection([
        ('alkes1', 'Alkes A'),
        ('alkes2', 'Alkes B'),
        ('alkes3', 'Alkes C'),
        ('chiller1', 'Chiller A'),
        ('chiller2', 'Chiller B'),
        ('chiller3', 'Chiller C'),
        ('lemari1', 'Lemari Steril A'),
        ('lemari2', 'Lemari Steril B'),
        ('lemari3', 'Lemari Steril C'),
        ('palet1', 'Palet Consumable A'),
        ('palet2', 'Palet Consumable B'),
        ('palet3', 'Palet Consumable C'),
        ('loker1', 'Loker Obat A'),
        ('loker2', 'Loker Obat B'),
        ('loker3', 'Loker Obat C')
    ], string='Rak', default='alkes1', required=True)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('sku_unique', 'unique(sku)', 'SKU must be unique!'),
    ]